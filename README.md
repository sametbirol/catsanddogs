# Project Name

Social Media Webpage for cats and dogs!
Technologies:FastAPI,Vuejs,Vuetify

## Table of Contents
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [SQLAlchemy Database Setup](#sqlalchemy-database-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to set up and run the project locally.

### Backend Setup

1. Navigate to the backend directory:

>cd backend/src


2. Create and activate a virtual environment (Optional, but recommended):

>python -m venv venv

>source venv/bin/activate

>On Windows: venv\Scripts\activate


3. Install the required dependencies:
>pip install -r requirements.txt


### Frontend Setup

1. Navigate to the frontend directory:

>#from root

>cd frontend

>#from backend/src directory

>cd ../../frontend


2. Install Node.js dependencies:
>npm install

### SQLAlchemy Database Setup

1. Simply change the URL in database.py file found at backend/src directory:
> your sqlalchemy databse url goes here
> postgresql://postgres:PASSWORD@localhost/DATABASENAME


## Usage

1. Start the backend server:

>#from root

>cd backend/src

>#from frontend directory

>cd ../backend/src


>uvicorn main:app --reload


2. Start the frontend development server:
>#from root

>cd frontend

>#from backend/src directory

>cd ../../frontend


>npm run dev


3. Open your web browser and access the application at http://localhost:3000/.


