TrackHack
==========

Track it ship it.

[Live demo here](http://enigmatic-badlands-3535.herokuapp.com/)


## Setting up

#### virtualenv

Install the latest version of _virtualenv_. You can get it from here: https://pypi.python.org/pypi/virtualenv

Clone the repo. We assume you've cloned it to a folder named `$HACKTRACK_HOME`. Navigate to `$HACKTRACK_HOME` and create a new virtual environment `thenv`.

	$> cd /path/to/$TRACKHACK_HOME
	$> virtualenv thenv

Activate the environment:

	$> source thenv/bin/activate

You should see `(thenv)` prepended to your prompt, indicating the environment has been activated.

Just for reference: You can type `deactivate` from anywhere to deactivate the environment.

#### Install dependencies

Navigate to $TRACKHACK_HOME and install the required packages from requirements.txt

	$> pip install -r requirements.txt

#### Setup database url environment variable

You will have to put the url in of your mongo database in `TH_MONGO_URL` variable in your environment.
