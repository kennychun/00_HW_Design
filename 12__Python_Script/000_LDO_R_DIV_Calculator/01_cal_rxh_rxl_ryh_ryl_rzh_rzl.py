
#	NOTE : FAIL
#
#		GPIO can be 0.0V or 3.3V
#		But, Vout should be 3.3V, 2.5V, 1.8V
#		Pull-up / pull-down with GPIO will not work in a simple way. 
#

print("ABCD")
mts_e3  = [	1.0,  2.2,  4.7                            ]
mts_e6  = [	1.0,  1.5,  2.2,  3.3,  4.7,  6.8          ]
mts_e12 = [	1.0,  1.2,  1.5,  1.8,  2.2,  2.7,  3.3,  3.9,  4.7,  5.6,   \
		6.8,  8.2     ]
mts_e24 = [	1.0,  1.1,  1.2,  1.3,  1.5,  1.6,  1.8,  2.0,  2.2,  2.4,   \
		2.7,  3.0,  3.3,  3.6,  3.9,  4.3,  4.7,  5.1,  5.6,  6.2,   \
		6.8,  7.5,  8.2,  9.1     ]
mts_e48 = [ 	1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54,  \
		1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49,  \
		2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02,  \
		4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49,  \
		6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53 ]

mts_e96 = [	1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, \
		1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, \
		1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, \
		2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, \
		2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, \
		3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12, \
		4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, \
		5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, \
		6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, \
		8.66, 8.87, 9.09, 9.31, 9.53, 9.76 ]

mts_e192 = [	1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11, \
		1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24, 1.26, \
		1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, \
		1.43, 1.45, 1.47, 1.49, 1.50, 1.52, 1.54, 1.56, 1.58, 1.60, \
		1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.80, \
		1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2.00, 2.03, \
		2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, \
		2.32, 2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, \
		2.61, 2.64, 2.67, 2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91, \
		2.94, 2.98, 3.01, 3.05, 3.09, 3.12, 3.16, 3.20, 3.24, 3.28, \
		3.32, 3.36, 3.40, 3.44, 3.48, 3.52, 3.57, 3.61, 3.65, 3.70, \
		3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.02, 4.07, 4.12, 4.17, \
		4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70, \
		4.75, 4.81, 4.87, 4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.30, \
		5.36, 5.42, 5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.90, 5.97, \
		6.04, 6.12, 6.19, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, \
		6.81, 6.90, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.50, 7.59, \
		7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56, \
		8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53, 9.65, \
		9.76, 9.88 ]


mts_use_base  = mts_e192
mts_use_x10   = [x*10  for x in mts_use_base]
mts_use_x100  = [x*100 for x in mts_use_base]

mts_use = mts_use_base
mts_use.extend ( mts_use_x10  )
mts_use.extend ( mts_use_x100 )
print ( ' '.join(["{:.2f}".format(x)  for x in mts_use]))

mts_len = len (mts_use )

#index = mts_use.index ( 9.88)
#print (index)


def find_index(arr, value, tolerance=1e-9):
    for i, x in enumerate(arr):
        if abs(x - value) < tolerance:
            return i
    return None

#   -------|                                              -------|                                          -------|                                                                
#     vout |--------------------------------  V3.3          vout |--------------------------------  V2.5      vout |--------------------------------  V1.8
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#          |     rxh      ryh      rzh                           |     rxh      ryh      rzh                       |     rxh      ryh      rzh            
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#     vref |-------------------------                       vref |-------------------------                   vref |-------------------------             
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#          |     rxl      ryl      rzl                           |     rxl      ryl      rzl                       |     rxl      ryl      rzl            
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#          |     |        |        |                             |     |        |        |                         |     |        |        |              
#   -------|    ---      ---      ---                     -------|    ---      ---      ---                 -------|    ---      ---      ---             
#               GND      IO0.0    IO0.0                               GND      IO3.3    IO0.0                           GND      IO0.0    IO3.3           
#                                    
#   Initial rough calculation
#	Step 1. to make simpe, rxh:rxl = ryh:ryl = rzh:rzl = 7.25:1 
#		- Vout = 0.4 * ( 1 + 7.25 ) = 3.3
#		  -> ryh = ryl * 7.25, rzh = rzl*7.25
#		- rxl =    1K ohm
#		- rxh = 7.32K ohm	( e192 resistor, 7.32K is the closest one to 7.25K )
#		- ryh = 7.25y
#		- ryl = y
#		- rzh = 7.25z
#		- rzl = z
#	Step 2. Calculate V2.5 case
#		R_H = 1/ (1/rxh + 1/ryh + 1/rzh + 1/ryl)
#		R_L = 1/ (1/rxl +         1/rzl        )
#		Set equation with y and z : Vout = 0.4 * ( 1 + R_H/R_L ) = 5.25
#	Step 3. Calculate V1.8 case
#		R_H = 1/ (1/rxh + 1/ryh + 1/rzh + 1/rzl)
#		R_L = 1/ (1/rxl + 1/ryl                )
#		Set equation with y and z : Vout = 0.4 * ( 1 + R_H/R_L ) = 3.50

idxh = find_index ( mts_use, 7.32 )
idxl = find_index ( mts_use, 1.00 )
idyh = find_index ( mts_use, 137  )
idyl = find_index ( mts_use, 19.1 )
idzh = find_index ( mts_use, 53.6 )
idzl = find_index ( mts_use, 7.32 )


idxh_min = idxh-5 if idxh > 5     else 0
idxl_min = idxl-5 if idxl > 5     else 0
idyh_min = idyh-5 if idyh > 5     else 0
idyl_min = idyl-5 if idyl > 5     else 0
idzh_min = idzh-5 if idzh > 5     else 0
idzl_min = idzl-5 if idzl > 5     else 0

idxh_max = idxh+5 if idxh < mts_len-5     else mts_len-1
idxl_max = idxl+5 if idxl < mts_len-5     else mts_len-1
idyh_max = idyh+5 if idyh < mts_len-5     else mts_len-1
idyl_max = idyl+5 if idyl < mts_len-5     else mts_len-1
idzh_max = idzh+5 if idzh < mts_len-5     else mts_len-1
idzl_max = idzl+5 if idzl < mts_len-5     else mts_len-1


print ( "----------------------------------------" )
print ( "idxh = ", idxh_min , idxh , idxh_max )
print ( "idxl = ", idxl_min , idxl , idxl_max )
print ( "idyh = ", idyh_min , idyh , idyh_max )
print ( "idyl = ", idyl_min , idyl , idyl_max )
print ( "idzh = ", idzh_min , idzh , idzh_max )
print ( "idzl = ", idzl_min , idzl , idzl_max )
print ( "----------------------------------------" )

for m in range (0,6):
	(i_min, i, i_max) = (	(idxh_min, idxh, idxh_max) if m==0 else
				(idxl_min, idxl, idxl_max) if m==1 else
				(idyh_min, idyh, idyh_max) if m==2 else
				(idyl_min, idyl, idyl_max) if m==3 else
				(idzh_min, idzh, idzh_max) if m==4 else
				(idzl_min, idzl, idzl_max) if m==5 else
				( 0, 0, 0 )
	)
	
	print ( f'r : ({i_min:3},{i:3},{i_max:3})' , end=" ")
	for r in (mts_use[n] for n in range (i_min, i_max+1) ):
		print (format(r, "6.2f"), end="  ")
	print (" " )

v_tol=0.0005

for rxh in (mts_use[n] for n in range (idxh_min, idxh_max+1) ):

	for rxl in (mts_use[n] for n in range (idxl_min, idxl_max+1) ):

		for ryh in (mts_use[n] for n in range (idyh_min, idyh_max+1) ):

			for ryl in (mts_use[n] for n in range (idyl_min, idyl_max+1) ):

				for rzh in (mts_use[n] for n in range (idzh_min, idzh_max+1) ):

					for rzl in (mts_use[n] for n in range (idzl_min, idzl_max+1) ):
					
						rh_33 = ( 1 ) / ( ( 1/rxh) + (1/ryh) + (1/rzh) ) 
						rl_33 = ( 1 ) / ( ( 1/rxl) + (1/ryl) + (1/rzl) ) 

						rh_25 = ( 1 ) / ( ( 1/rxh) + (1/ryh) + (1/rzh) + 1/(ryl) ) 
						rl_25 = ( 1 ) / ( ( 1/rxl)           + (1/rzl) ) 

						rh_18 = ( 1 ) / ( ( 1/rxh) + (1/ryh) + (1/rzh) + 1/(rzl) ) 
						rl_18 = ( 1 ) / ( ( 1/rxl) + (1/ryl)           ) 

						v33 = 0.4 * ( 1 + rh_33/rl_33)
						v25 = 0.4 * ( 1 + rh_25/rl_25)
						v18 = 0.4 * ( 1 + rh_18/rl_18)

						if (abs(v33-3.3)<v_tol) and abs(v25-2.5)<v_tol and abs(v18-1.8)<v_tol:
							print ( f"{rxh:6.2f} {rxl:6.2f} {ryh:6.2f} {ryl:6.2f} {rzh:6.2f} {rzl:6.2f}    {v33:8.5f} {v25:8.5f} {v18:8.5f}     {v33-3.3:8.5f} {v25-2.5:8.5f} {v18-1.8:8.5f}" )










#	print ("a        ", end="")
#	for mts1 in mts_use:
#		print( format(mts1,"5.2f"), end ="  " )
#	print ("")
#	
#	for mts0 in mts_use:
#		print ( format(mts0,"5.2f") , end ="    ")
#	
#		for mts1 in mts_use:
#			print ( format(1+mts0/mts1, "5.2f") , end ="  ")
#		print ("")
#		
#	for mts0 in mts_use:
#		print ( format(mts0*10,"5.2f") , end ="    ")
#	
#		for mts1 in mts_use:
#			print ( format(1+mts0*10/mts1, "5.2f") , end ="  ")
#		print ("")
#		
#	
#	
#	print ("")
#	print ("")
#	print ("a        ", end="")
#	for mts1 in mts_use:
#		print( format(mts1,"5.2f"), end ="  " )
#	print ("")
#	
#	for mts0 in mts_use:
#		print ( format(mts0,"5.2f") , end ="    ")
#	
#		for mts1 in mts_use:
#			print ( format(0.4*(1+mts0/mts1), "5.2f") , end ="  ")
#	
#		print ("")
#	
#	for mts0 in mts_use:
#		print ( format(mts0*10,"5.2f") , end ="    ")
#	
#		for mts1 in mts_use:
#			print ( format(0.4*(1+mts0*10/mts1), "5.2f") , end ="  ")
#		print ("")
#		
