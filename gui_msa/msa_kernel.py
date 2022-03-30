#!/usr/bin/env python
import subprocess
import os
import shlex
import sys

import time

if sys.version_info > (3, 0):
	raw_input = input

class MSA_Func:
    def __init__(self):
        self.outputs = {}



    def load_meta(self, fname):
        return
    
    def cl(self, command):
        #ip::string, command line as string input
        #op::string, return value is the output of command line
        #Notice, each time when change directly, cl starts from currect directory.
        #Use three \' if you want to input multiple line
        arg = shlex.split(command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        return output

    # read data
    def read_data(self, order, symmetry, train_x):
        
        arg = order +' '+ symmetry
        self.cl('''
        cd src
        cd emsa
        make
        cp msa ../
        cd ../
        ./msa '''+ arg +  '''
        perl postemsa.pl ''' + arg + '''
        perl derivative.pl ''' + arg + '''
        '''
        )
        f = open(train_x)
        nol = 0
        for line in f:
          nol=nol+1
          if nol==1:
            natom=int(line)
        nconfig = nol/(natom+2)
        f.close()        
        
        #  natom, nconfig
        f = open('./src/basis.f90')
        nol=1 #Num of lines in file
        for line in f:
          if nol==8:
            ncoeff = int(line.split(':')[1].split(')')[0])
            ncoeff = ncoeff + 1
          if nol==24:
            nmonomial = int(line.split(':')[1].split(')')[0])
            nmonomial = nmonomial + 1
            break
          nol=nol+1
        f.close()
        
        # order, symmetry, ncoeff
        
        self.update_data(train_x, nmonomial, natom, nconfig, order, 
                         symmetry, ncoeff)
        
        
        
    # udpate dictionary values
    def update_data(self, train_x, nmonomial, natom, nconfig, order, symmetry, ncoeff):
               
        self.outputs["natom"] = natom
        self.outputs["nconfig"] = nconfig
        self.outputs["order"] = order
        self.outputs["symmetry"] = symmetry
        self.outputs["ncoeff"] = ncoeff    
        self.outputs["nmonomial"] = nmonomial 
        self.outputs["train_x"] = train_x


    def update_wt(self, wt): 
        self.outputs["wt"] = wt
    
    def update_a0(self, a0):    
        self.outputs["a0"] = a0    
    
    def process(self):
        
        g = open('./src/fit.f90','w')
        g.write('''program fit
        use basis
        implicit none
        
          external dgelss
          real :: rmse, wrmse, a0, dwt, vmin
          integer :: data_size
          real,allocatable::xyz(:,:,:),x(:)
          real,allocatable::v(:),b(:),p(:),wt(:)
          real,allocatable::yij(:,:), A(:,:)
          real,allocatable::coeff(:),v_out(:),s(:)
          real :: work(150000), dr(3)
          integer :: ncoeff, natm, ndis
          integer :: i, j, k, m, info, rank
          character(len=32) :: data_file
          character :: symb
        
          natm=''' + str(self.outputs["natom"]) + '''         ! change to the number of atoms
          ncoeff=''' + str(self.outputs["ncoeff"])+ '''       ! change to the number of coeff. (size of c in bemsa.f90)
          data_size=''' + str(self.outputs["nconfig"])+ '''    ! change to the number of data points in pts.dat
          a0=''' + self.outputs["a0"] + '''
          dwt=''' + self.outputs["wt"] + '''
        
          ndis=natm*(natm-1)/2
        
          open(10,file="coeff.dat",status='unknown')
          open(11,FILE="points.eng",status='unknown')
          open(12,file="'''+self.outputs["train_x"]+'''",status='old')
          open(13,file="output.txt",status="unknown")
        
          allocate(x(ndis))
          allocate(xyz(data_size,natm,3))
          allocate(v(data_size),v_out(data_size),b(data_size),coeff(ncoeff),s(ncoeff))
          allocate(yij(data_size,ndis))
          allocate(p(ncoeff))
          allocate(A(data_size,ncoeff))
          allocate(wt(data_size))
        
          do i=1,data_size
             read(12,*)
             read(12,*) v(i)
             do j=1,natm
                read(12,*) symb,xyz(i,j,:)
             end do
          end do
          vmin = minval(v)
        
          do m=1,data_size
             k = 1
             do i=1,natm-1
                do j=i+1,natm
        
                   yij(m,k)=0.0
                   dr=xyz(m,i,:)-xyz(m,j,:)
                   yij(m,k)=sqrt(dot_product(dr,dr))
                   yij(m,k)=yij(m,k)/0.5291772083
                   yij(m,k)=exp(-yij(m,k)/a0)
        
                   k=k+1
                end do
             end do
          end do
        
          do i=1,data_size
             wt(i)=dwt/(dwt+v(i)-vmin)
             x=yij(i,:)
             call bemsav(x,p)
             A(i,:)=p*wt(i)
             b(i)=v(i)*wt(i)
          end do
        
          call dgelss(data_size,ncoeff,1,A,data_size,b,data_size,s,1.0d-8,rank,work,150000,info)
          coeff(:)=b(1:ncoeff)
        
          do i=1,ncoeff
             write(10,*) coeff(i)
          end do
        
          rmse=0.0
          wrmse=0.0
          do i=1,data_size
             v_out(i)=emsav(yij(i,:),coeff)
             write (11,*) v(i),v_out(i),abs(v(i)-v_out(i))*219474.63
             rmse=rmse+(v(i)-v_out(i))**2
             wrmse=wrmse+(wt(i)*(v(i)-v_out(i)))**2
          end do
        
          rmse=sqrt(rmse/dble(data_size))
          wrmse=sqrt(wrmse/dble(data_size))
          write(*,'(A)') '3. Fitting is finished: '
          write(*,'(A,F15.10,A)') 'Overall Root-mean-square fitting error: ', rmse , ' Hartree'
          write(*,'(A,F15.10,A)') 'Weighted Root-mean-square fitting error: ', wrmse , ' Hartree'
          write(13,'(F15.10)') rmse
          write(13,'(F15.10)') wrmse
        
          deallocate(xyz,x,v,b,p,yij,A,coeff,v_out,s,wt)
          close (10)
          close (11)
          close (12)
          close (13)
        
        end program
        ''')
        g.close() #Must close the file handle if you want to compile this file.
        
        self.cl('''
        cd src
        sed 's/a = 2.5d0/a = ''' + self.outputs["a0"] + '''/g' gradient.f90 > temp.f90
        mv temp.f90 gradient.f90
        make
        ''')
        
        # print("Fitting... (This might take time) \n")
        
        self.cl('''cp ./src/fit.x ./
        ./fit.x '''+self.outputs["train_x"]+'''
        rm fit.x
        mv ./src/basis.f90 ./
        mv ./src/gradient.f90 ./
        cp ./src/Makefile ./
        cp ./src/getpot.f90 ./ '''
        )
        
        g = open('pes_shell.f90','w')
        g.write('''module pes_shell
        use basis
        use gradient
        implicit none
        
          real::coeff(1:'''+str(self.outputs["ncoeff"])+''') ! change to number of coefficients
                             ! (size of c in bemsa.f90)
          save coeff
        
        contains
          !==================================!
          ! read the coefficients of the PES !
          !==================================!
          subroutine pes_init()
            !::::::::::::::::::
            integer::i
        
            open(10,file='coeff.dat',status='old')
        
            do i=1,size(coeff)
               read (10,*) coeff(i)
            end do
        
            return
            close (10)
          end subroutine pes_init
        
          !====================================!
          ! Function to evaluate the potential !
          !====================================!
          function f(xyz)
            real,dimension(:,:),intent(in)::xyz
            real::f
            !::::::::::::::::::::::::::::::
            real,dimension(size(xyz,2)*(size(xyz,2)-1)/2)::x
            real,dimension(3)::dr
            real::a0  ! the same as the fitting code
            integer::i,j,k
        
            a0 = ''' + self.outputs["a0"] + '''
        
            k = 1
            do i=1,size(xyz,2)-1
               do j=i+1,size(xyz,2)
                  dr = xyz(:,i) - xyz(:,j)
                  x(k) = sqrt(dot_product(dr,dr))
                  k = k+1
               end do
            end do
        
            do i=1,size(x)
               x(i)=exp(-x(i)/a0)
            end do
        
            f=emsav(x,coeff)
        
            return
          end function f
        
          !===========================!
          ! function to calculate the !
          ! analytical gradient       !
          !===========================!
          function g(xyz)
            real,dimension(:,:),intent(in)::xyz
            real,dimension(size(xyz,2)*3)::g
            !::::::::::::::::::::
            real,dimension(size(xyz,2)*(size(xyz,2)-1)/2)::r,x
            real,dimension(3,size(xyz,2)*(size(xyz,2)-1)/2)::dr
            real,dimension(size(xyz,2)*3,size(xyz,2)*(size(xyz,2)-1)/2)::drdx
            real,dimension(1:''' + str(self.outputs["ncoeff"]) + ''')::p   ! change to number of popynomials
                                       ! (size of p in bemsa.f90)
            real,dimension(1:'''+str(self.outputs["nmonomial"])+''')::m  ! change to number of monomials
                                      ! (size of m in bemsa.f90
            real::a0
            integer::i,j,k
        
            a0 = ''' + self.outputs["a0"] + '''
        
            k = 1
            drdx = 0.d0
            do i=1,size(xyz,2)-1
               do j=i+1,size(xyz,2)
                  dr(:,k) = xyz(:,i) - xyz(:,j)
                  r(k) = sqrt(dot_product(dr(:,k),dr(:,k)))
        
                  drdx(3*i-2:3*i,k) = dr(:,k)/r(k)
                  drdx(3*j-2:3*j,k) = -drdx(3*i-2:3*i,k)
                  k = k+1
               end do
            end do
        
            do i=1,size(x)
               x(i)=exp(-r(i)/a0)
            end do
        
            call evmono(x,m)
            call evpoly(m,p)
        
            do i=1,3*size(xyz,2)
               g(i) = demsav(drdx,coeff,m,p,i)
            end do
        
            return
          end function g
        
        end module pes_shell
        ''')
        g.close()
        
        self.cl('''make getpot.x
        cp ./src/test.xyz ./
        cp ./src/expected.out ./'''
        )
        
    def extract_rmse(self):
        with open('temp_rmse.txt') as f:
            lines = f.readlines()
        rmse = lines[0]
        wrmse = lines[1]
        self.outputs["rmse"] = rmse
        self.outputs["wrmse"] = wrmse
        
        
        
        