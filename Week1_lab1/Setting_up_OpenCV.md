# How to set up OpenCV  

On new terminal in VS Code:  
Step 1: Go to the desired directory then create the virtual environment and in terminal input the following line:  
`python3 -m venv myvenv`  
  
Step 2: Activate the virtual environment using (this line is for Mac):  
`source myvenv/bin/activate`  

Step 3: Install OpenCV within the virtual environment:  
`pip install opencv-python`  

## Notes about the virtual environment
1. Virtual environments create a separate environment with its own python libraries for each project. Each project will have their own dependencies within the same machine.  
2. Avoid global installation.  
3. All the subfolder within where the virtual environment is installed will be under the same virtual environment.
4. Virtual environments need to be activated every time when in a new terminal session. Using the code in step 2 to activate.