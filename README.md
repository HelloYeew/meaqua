# meaqua
 Startpage for your browser with built-in editors, full customization and built-in style sharing system.

## Origins
This project take an idea from [Flame](https://github.com/pawelmalak/flame) that's a good start page for your browser, but I need to add more 
of my styling and some customization, so I forked and use my forked repository for half a year now. But I think that if we make 
it better like add more customization ,some styling sharing system, more editor, and you don't need to hosted it yourself anymore.
That's why this project has been created.

## Current Status
This project is still in development, but it can be use for personal use now by control your styling in Django's admin theme. I will use this as backend and will rewrite frontend in maybe Svelte or React.

## Set up the project
### Step 1: Cloning the Repository
There are two ways to go about it, one being downloading as a zip file and the other being cloning via git command line. We will guide you through the latter method since the former is pretty straight forward (download and extract files).

Navigate to your desired directory, then clone the **meaqua** repository by entering the following command into your git command line:
```
git clone https://github.com/HelloYeew/meaqua.git
```

### Step 2: Setting Up the Environment
First and foremost, we need to create a virtual environment for this project. We will use virtualenv in this case.

Install virtualenv by running as a global package via this command:
```
pip install virtualenv
```

Then navigate to `.../meaqua` and run the following command:
```
virtualenv [virtual environment name]
```

Now that you have your virtual environment set up, you can now activate the virtual environment by running either one of the following commands:

**Mac OS/Linux**
```
source [virtual environment name]/bin/activate
```

**Windows**
```
[virtual environment name]/Scripts/activate
```

After activating the virtual environment, to install all the required modules run the following command:
```
pip install -r requirements.txt
```

And that's all for Python. Now for Django, we have a tiny setup to do and we're golden.

### Step 3: Running the Server
Create a new `.env` from `.env.example` at the same place and fill in the required information.

Before running the server we have to migrate the database using the following command:
```
python manage.py migrate
```

Now try running the server! Run the command below:
```
python manage.py runserver
```

## Contributing
If you have some cool idea ot find some bugs in the project, please feel free to open an issue pr create a pull request and I will respond and review it as fast as I can!
