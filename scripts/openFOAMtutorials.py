import os, sys, subprocess

#Create the folders as described by the openFOAM tutorial
os.system('mkdir -p $FOAM_RUN') 

#Copy the example files
os.system('cp -r $FOAM_TUTORIALS $FOAM_RUN')

exampleDir = "%s/tutorials/incompressible/icoFoam/cavity" % (os.environ['FOAM_RUN'])

print """
To run the examples, go i.e. to %s and type the following:

blockMesh
icoFoam
paraFoam

If you want to execute these commands now, type 'exec'. If you want to quit, type 'quit'.
""" % exampleDir 

reLoop = True
while reLoop:
    inArg = raw_input()

    if inArg == "exec":
        os.chdir(exampleDir)
        for example in ['blockMesh','icoFoam','paraFoam']: subprocess.call(example)
        reLoop = False	

    elif inArg == "quit":
        sys.exit(1)
    else:
        print "Invalid argument provided. Type either 'exec' or 'quit'."
