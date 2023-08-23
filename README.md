# **Season to Taste**
WHY I BUILT/ MADE THIS WEBSITE

![Responsive screenshot showing site on different screen sizes]()

[Deployed site]()

# **Table Of Contents**
* [**Season-to-Taste**](#season-to-taste)
* [**Planning Phase**](#planning-phase)
  * [**Strategy**](#strategy)
    * [**Site Aims:**](#site-aims)
  * [**Structure**](#structure)
    * [**User Stories:**](#user-stories)
    * [**User Stories dropped as part of the agile process**](#user-stories-dropped-as-part-of-the-agile-process)
  * [**Skeleton**](#skeleton)
    * [**Wireframes:**](#wireframes)
    * [**Database Schema**](#database-schema)
  * [**Surface**](#surface)
    * [**Color scheme:**](#color-scheme)
    * [**Typography**:](#typography)
      * [***Condiment:***](#condiment)
      * [***Lato:***](#lato)
* [**Agile Development Process**](#agile-development-process)
* [**Features**](#features)
  * [**Site Navigation**](#site-navigation)
    * [**Navbar**](#navbar)
      * [***Logo:***](#logo)
      * [***Signed Out:***](#signed-out)
      * [***Signed In:***](#signed-in)
      * [***Hamburger menu on smaller screen sizes:***](#hamburger-menu-on-smaller-screen-sizes)
    * [**Hero Images:**](#hero-images)
      * [***Job Openings/Landing Page:***](#job-openingslanding-page)
      * [***Add Job Form Page:***](#add-job-form-page)
    * [***Saved jobs page:***](#saved-jobs-page)
    * [***Insights page:***](#insights-page)
    * [***Edit note form page:***](#edit-note-form-page)
  * [**AllAuth Pages**](#allauth-pages)
    * [***Sign In:***](#sign-in)
      * [***Form Errors:***](#form-errors)
    * [***Sign Up:***](#sign-up)
      * [***Form Errors:***](#form-errors-1)
    * [***Sign Out:***](#sign-out)
  * [**Site Instructions**](#site-instructions)
    * [***Access to instructions page:***](#access-to-instructions-page)
      * [***Nav link:***](#nav-link)
      * [***On page Button:***](#on-page-button)
      * [***Note form Anchor tag:***](#note-form-anchor-tag)
  * [**Main Page Content**](#main-page-content)
    * [***Job Openings page:***](#job-openings-page)
      * [***Add Job Button:***](#add-job-button)
      * [***Add Job Form:***](#add-job-form)
      * [***Add Job Success message:***](#add-job-success-message)
    * [***Job Openings and Pinned Board Content:***](#job-openings-and-pinned-board-content)
      * [***Job Preview Card (logged out):***](#job-preview-card-logged-out)
      * [***Job Preview Card (Logged in):***](#job-preview-card-logged-in)
      * [***Job Preview Card Footer (Logged in as admin user):***](#job-preview-card-footer-logged-in-as-admin-user)
    * [***Full Job Details Page***](#full-job-details-page)
      * [***Full details card (unpinned):***](#full-details-card-unpinned)
      * [***Full details card (pinned):***](#full-details-card-pinned)
        * [**Full job card**](#full-job-card)
      * [***Notes form:***](#notes-form)
      * [***Notes Accordion:***](#notes-accordion)
        * [**Note:**](#note)
        * [**Insight:**](#insight)
    * [***Insights PAge:***](#insights-page-1)
      * [***Add Insight Button:***](#add-insight-button)
      * [***Add Insight Form:***](#add-insight-form)
      * [***Add Insight Form Errors:***](#add-insight-form-errors)
        * [**Short description field error:**](#short-description-field-error)
        * [**Short description field error:**](#short-description-field-error-1)
      * [***Insight left success message:***](#insight-left-success-message)
      * [***Insight Item Display:***](#insight-item-display)
      * [***Timeline:***](#timeline)
    * [***Contact Us Page:***](#contact-us-page)
    * [***Pagination:***](#pagination)
    * [***Footer:***](#footer)
  * [**Error pages**](#error-pages)
    * [***Members Only Page:***](#members-only-page)
    * [***500 Server Error Page:***](#500-server-error-page)
    * [***404 Page Not Found Error Page:***](#404-page-not-found-error-page)
  * [**Warning Modals**](#warning-modals)
    * [***Delete Note/Insight:***](#delete-noteinsight)
    * [***Delete Job:***](#delete-job)
    * [***Unpin Job:***](#unpin-job)
    * [***Delete element from the DOM:***](#delete-element-from-the-dom)
* [**Future development**](#future-development)
* [**Testing Phase**](#testing-phase)
* [**Deployment**](#deployment)
* [**Technologies used**](#technologies-used)
* [Honorable mentions](#honorable-mentions)
* [Credits](#credits)

# **Planning Phase**
## **Strategy** 
### **Site Aims:**
### **Research:**
  
## **Structure**   
To help me visualize a typical user journey around the site, I used [draw.io](https://app.diagrams.net/) to help me plan out the various routes a user could take through the site. This flow changed slightly throughout development. However, in general, it guided the process.
  
![User Journeys flow chart]()
  
### **User Stories:**  
  
* As an **Admin** I can...
 
* As an **Unregistered User** I can... 
  
* As a **Registered User** I can... 
 
* As a **Site User** I can...
  

## **Skeleton**
### **Wireframes:**
* [Homepage wireframes]()  
* [OTHER PAGE WIREFRAME ETC]()


### **Database Schema**
Below is my initial plan for my database tables:  

 
Within my models.py, I also have a function using the @receiver decorator to create a PinnedJobs object whenever a user registers; the object is user-specific and links a user to a many2many list of the user's pinned jobs within the PinnedJobs table. Later this can be further developed into a user profile.

## **Surface**
### **Color scheme:**
The final list of colors used has been placed in the below [color grid]() to check contrast scores.

![Color gird]()

### **Typography**:

# **Agile Development Process**
  
# **Features**
## **Site Navigation**
### **Navbar**
#### ***Logo:***

![Site Logo]()
  
#### ***Signed Out:***
#### ***Signed In:***
#### ***Hamburger menu on smaller screen sizes:***
To display the menu properly on smaller screen sizes, a burger menu was implemented using bootstrap.  
### **Hero Images:**
I picked the hero images to portray the page's theme to the user. 
## **AllAuth Pages**
### ***Sign In:***
![sign-in form]()
#### ***Form Errors:***
![Invalid log in credentials]()
### ***Sign Up:***
![sign-up form]()
#### ***Form Errors:***
![Form errors for sign up form]()
### ***Sign Out:***
![Sign out page]()

# **Future development**

# **Testing Phase**

# **Deployment**

# **Technologies used**

# Credits

* General references:
   
