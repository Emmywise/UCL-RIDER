# Tech Test: UCI Enduro World Cup Race Management

## 🎯 Objective
You’re building a simplified system for managing a Mountain Bike race.
Think of it as the digital nerve center for organizing the event—minus the mud, 
crashes, and mid-race mechanicals.

The race format is as follows:

Each Rider races for a team in a given age bracket

You will need to store data regarding the following:
* Rider
* Team
* Qualifying Race Result
* Main Race Result

## 🛠️ What You’ll Be Doing
* Modeling race data – riders, teams, qualifying times, race order and race results.
* Adding a way for privileged users to CRUD all data.
* Creating a way for members of the public to add themselves as riders.
* Displaying riders, teams and results – create a simple front end to make sure members of the public can see who’s
  racing and repping each squad and what their results are.
* Generating race-day rider start order – unlike other types of competition in this race the fastest qualifiers
  start the main race last!

The focus is on Django and back-end architecture, so we’re not expecting a full-blown UI masterpiece.
Just something functional to show off your work.


## 🚀 Getting Started
* Set up your virtual environment however you're comfortable.
  
> Note: Minimum python version required is 3.10.0
* Install requirements 
  ```bash
    pip install -r requirements.txt
  ```
* Run initial migrations
  >Note: A couple of models have been provided,
  >feel free to modify these as you wish. You will need to add more.

Now, let's get into it...
  
## Tasks:

### 📝 Task 0 - Boilerplate
Create a sensible schema to model the problem, create some test data and a way to get it into the database and then
create a way for privileged users to edit the data (Django Admin is fine).

### 🚵 Task 1 - Build the Rider Roster
Alright, time to get some teams on the board! Your first challenge is to display rider and team information in a
way that makes sense.

#### 🏁 Part A - The Lineup
Create a page that lists all riders, grouped by:

* Age category
  * You decide the brackets—something like ‘Under 12’, ‘Junior’, ‘Senior’ would make sense.
* Team affiliation.

#### 🔍 Part B - Filter the Field
Make it easy to drill down into the details. Add a way to search and filter riders by (at least):
* Name(s)
* Team
* Age category

There’s no single “right” way to do this—the approach is up to you. 
Pick whatever patterns and design choices make sense, and show us how you’d tackle it. 🚀

The only thing required is that it must be viewable on a webpage.


### 🏁 Task 2 - Race Day

Now that we’ve got our teams, let’s figure out who’s dropping in first on race day. 
Your job is to generate the official race start order based on riders qualifying times.

Before each race, each racer will run the course once and the time they complete it in will be
used as their qualifying time. This is used to determine the race order for the main race, as each
racer will ride the course sequentially, not all at the same time.

#### ⏱️ Part A - Qualifying Results
Each rider gets one qualifying race time to keep it simple, no multi-stage madness.
Store these times and make sure they’re tied to the correct rider.
We need a page to view these times, which should be sorted fastest first by default.

#### 🚦 Part B - Race Day Start Order
The fastest riders from qualifying actually race last on the big day.
Use the sorted qualifying results to generate a race order for the main race where the slowest qualifier
starts first and the fastest qualifier goes last.
How you structure the logic is up to you—that’s part of the challenge.
Show us how you’d approach it!

#### 🏆 Part C - Photo Finish
For the last part, we want to see who sent it the hardest and allow our top shredders to bask in their glory!
Store all race results for each rider and show us a page that shows the podium (🥇1st, 🥈2nd and 🥉3rd place)
for each age category of the race in any way you feel makes sense.

---

### 🎯 Want to Go the Extra Mile? (Optional, But Impressive):

If you’re feeling ambitious, here are some bonus features that would give your solution an 
extra layer of polish:

* 🛠️ Docker Setup 
  * Provide a docker-compose.yml to spin up Django easily.
  * Change the DBMS from SQLite to Postgres.
  * Include a Dockerfile for building and running the app smoothly.

* 🏆 Extra Features 
  * Rider profiles with photos and race history. 
  * Style the UI and impress us with your frontend skills.
  * Anything else that would make this feel like a proper race management tool—use your imagination!

---

## 📦 What You Need to Deliver:

1. **Models**:
   * Implement the necessary models as described.

2. **Data**:
   * Create some test data to allow us to test your features and provide a way (and instructions) for how we can
     load it into the database.
   * Ensure that the main race Run Order can be generated correctly based on the qualifying times.

3. **Basic Front-End**:
   * Provide a minimal front-end for members of the public to view all records and to create Rider records for
     themselves.
   * Create a way for authenticated users to CRUD all records (using Django Admin is acceptable).
   * The focus should be on functionality, not design.

4. **Instructions**:
   * A README with steps to install, run, and use the app.
   * If you add anything extra, make sure we know how to check it out!

---

## ⚙️ Technical Requirements:

* **Django** for the back-end.
* **SQLite** as the database.
* Minimal front-end (basic Django templates).

---

## 🔍 How You’ll Be Evaluated:

1. **Model Design** - Are the models structured well? Do they make sense for the problem?
2. **Functionality** - Does the system correctly handle rider data, race data, and run order generation? Is the code
   optimised in a way that it will scale well and does it minimise DB queries?
3. **Code Quality**
   * Is it clean, structured, and easy to follow?
   * Is it appropriately covered with tests?
   * Does it comply with PEP8?
4. **Front-End** - Does it allow interaction with the data without unnecessary friction?

---

## ⏳ Timeframe
This is a 3-hour challenge—keep it focused and don’t overthink it.
If anything takes longer or needs clarification, just make a note of it.
---

## 📩 Submission
Commit your code to a git repository as you go and when you’re done, send us:

* The URL to your repo - we like to see the commit history.
  * If you'd like to keep your repository private you can simply invite "t.jones" and 
  "jamiemayer523" (as "members" not "guests", since the guest role can't see repo code) to view your Gitlab repo, or 
  "ftstim" and "jamieb-fts" as collaborators to view your GitHub repo.
* Instructions on how to run the project.
* Any notes/assumptions you made along the way and any problems you encountered.

Good luck—now get coding! 🚀
