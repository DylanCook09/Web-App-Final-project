# Coding I – Web Application Project

**Due date:** 5/14 @ Midnight  

When you finish, add your names and a demo video link here, then submit one link to your project repository.

**Group Members:** Eli. B, Dylan. C, Elohim. M 
* [Demo Video (1 per group)](http://includeyourlinkhere)

---

### Project Overview

You will begin with a **pre-built login and authentication system**. Your job is to **extend this project into a full CRUD web application** using Flask and a database.

Your application must allow users to:
- Log in (already implemented)
- Create data
- View data
- Edit data
- Delete data

Each user should only be able to access and modify **their own data**.

---

### Helpful Links for This Unit:
 - [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLite Documentation](https://www.sqlite.org/docs.html)
 - [Bcrypt Documentation](https://pypi.org/project/bcrypt/)
 - [Regex Tutorial for Python](https://docs.python.org/3/library/re.html)
 - [GitHub Cheat-Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
 - [Flask Tutorial](https://www.youtube.com/watch?t=347&v=Z1RJmh_OqeA) (we are already in a virtual environment so ignore comments about env)

---

### Project Requirements:

---

### Part I: Setup & Understanding the Base Code (10 pts)
- XFork the provided repository.
- XSuccessfully run the starter project locally.
- XDemonstrate understanding of:
  - XWhere login happens
  - XHow users are stored
  - XHow routes/templates are structured
- XMake at least one small modification (e.g., change text on a page) to confirm setup is working.

---

### Part II: Planning Your CRUD App (10 pts)
- XDecide what your app will store (journal, listings, notes, etc.).
- XClearly define:
  - XWhat a “record”/“entry” looks like (fields in your database)
- XPlan required features:
  - XCreate
  - XRead
  - XUpdate
  - XDelete
- XSketch or describe:
  - XPages/routes you will need
  - XBasic user flow (what happens after login)
- XComplete `planning_and_design.txt`.

---

### Part III: Database for App Content (10 pts)
- XCreate a **new database table** (separate from users).
- XInclude appropriate fields (e.g., title, content, timestamp, user_id).
- XEnsure:
  - XData persists after restarting the app
  - XEach entry is linked to a specific user

---

### Part IV: READ – Display Data (10 pts)
- XAfter login, users are taken to a **main page/dashboard**.
- XThis page displays a list of entries from the database.
- Requirements:
  - XData is clearly formatted
  - XOnly shows entries belonging to the logged-in user
  - XPage updates correctly when new data is added

---

### Part V: CREATE – Add New Entries (10 pts)
- XProvide a form/page to create new entries.
- On submission:
  - XData is saved to the database
  - XEntry is linked to the logged-in user
- XUser is redirected back to the main page and sees the new entry.

---

### Part VI: UPDATE – Edit Entries (10 pts)
- XUsers can edit existing entries.
- Requirements:
  - XEdit form pre-fills with current data
  - XChanges are saved to the database
  - XOnly the owner can edit their entries

---

### Part VII: DELETE – Remove Entries (10 pts)
- XUsers can delete entries.
- Requirements:
  - XEntry is removed from the database
  - XOnly the owner can delete their entries
  - X(Optional but encouraged) confirmation before deletion

---

### Part VIII: User Data Protection & Access Control (5 pts)
- Users cannot:
  - XView other users’ data
  - XEdit or delete entries they do not own
- XProper checks are implemented in routes (not just hidden buttons).

---

### Part IX: Reflection + Demo Video (25 pts)
- Demo must show:
  - Creating, viewing, editing, deleting entries
  - Login working with your CRUD system
  - All team members must speak
- Reflection includes:
  - What was hardest to implement
  - One bug or issue you solved
  - One improvement you would add

---

### Optional Bonus (+10 pts each)
- Add search, filtering, or sorting
- XImprove UI with CSS
- Add timestamps or ordering (newest first)
- Add categories/tags

---

### Key Focus of This Project
- You are no longer **building authentication**
- You are **building a functional database-driven application**

The most important part of this project is:
- Implementing full CRUD functionality
- Connecting data to the logged-in user
- Managing and displaying database content properly
