# Lecture Notebooks  
* Lecture notebooks are organized by classes, in each respective folder.  
* The requirements.txt file can be used to install all the necessary packages for all the notebooks in this course.

------------------

## Environment creation and installation
You're free to do this any other way if you're comfortable, but we recommend the below:
1) Install Anaconda from https://www.anaconda.com/download. You can refer to https://docs.anaconda.com/free/anaconda/install/index.html for installation instructions. MAKE SURE TO DOWNLOAD THE APPROPRIATE ONE FOR YOUR OPERATING SYSTEM.
2) Once anaconda is downloaded and the conda command is working in your terminal (refer to installation instructions), confirm that `conda activate base` command works (this should activate your base environment).
3) Run the following (replace \<your-environment-name> with a name for your environment, I used DSC232r):  
```bash
conda create -n <your-environment-name> python=3.6
conda activate <your-environment-name>
```
4) Make sure you have git installed, and an account with GitHub. Download this repository via git (https://github.com/ucsd-dsc232r-s24/lecture-notebooks.git). You can run the following command on terminal, in the location where you want to clone the repository.
```bash
git clone https://github.com/ucsd-dsc232r-s24/lecture-notebooks.git
```
5) Navigate to the folder location where you have downloaded this repository. Then, run 
```bash
pip install -r requirements.txt
```
This should create your environment with all necessary packages.