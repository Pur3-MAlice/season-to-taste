# **Season to Taste**
WHY I BUILT/ MADE THIS WEBSITE

![Responsive screenshot showing site on different screen sizes]()

[Deployed site]()

# **Table Of Contents**
* [**Season-to-Taste**](#season-to-taste)
* [**Planning Phase**](#planning-phase)
  * [**Site Aims**](#site-aims)
  * [**Research**](#research)
  * [**Structure**](#structure)
  * [**Skeleton**](#skeleton)
  * [**Surface**](#surface)
* [**Agile Development Process**](#agile-development-process)
* [**Features**](#features)
  * [**Site Navigation**](#site-navigation)
  * [**AllAuth Pages**](#allauth-pages)
  * [**Site Instructions**](#site-instructions)
  * [**Main Page Content**](#main-page-content)
  * [**Error pages**](#error-pages)
  * [**Warning Modals**](#warning-modals)
* [**Future development**](#future-development)
* [**Testing Phase**](#testing-phase)
* [**Deployment**](#deployment)
* [**Technologies used**](#technologies-used)
* [Credits](#credits)

# **Planning Phase**
## **Strategy** 
### **Site Aims:**
### **Research:**
One of the first things I did when building the plan for this website was research. I wanted my website, not only to be useable and have a solid logic base but for it also to look modern and inviting. So part of my Planning Phase was not only wireframing, building a logic flow chart and a database schema. But also looking at websites with similar aims, and discussing with friends and family how they use recipe websites. What do they like, what do they dislike, and how can I emulate the good parts whilst removing the annoyance?  
Here are some of the sites I used for inspiration for the design of Season To Taste:
* [thehappyfoodie](https://thehappyfoodie.co.uk/)
* [cookbookmanager](https://cookbookmanager.com/pricing)
* [Resturant Website Templates from Wix](https://www.wix.com/website/templates/html/restaurants-food)
  
  
  
## **Structure**   
To help me visualize a typical user journey around the site, I used [draw.io](https://app.diagrams.net/) to help me plan out the various routes a user could take through the site. This flow changed slightly throughout development. However, in general, it guided the process.
  
![User Journeys flow chart]()
  
### **User Stories:**  
  
* As an **Admin** I can...
 
* As a **Site User** I can...
  

## **Skeleton**
### **Wireframes:**
* [Homepage wireframes]()  
* [OTHER PAGE WIREFRAME ETC]()


### **Database Schema**
Below is my initial database schema to map out the relations between users, recipes, comments and categories (also known as tags). This is a rough idea of what the database will look like in general, but at this point in the planning phase, I understand that this is subject to change. So I will also be showing a representation of the Database here once the project is ready for deployment.
![Color grid]()
 
## **Surface**
### **Color scheme:**
The final list of colors used has been placed in the below [color grid]() to check contrast scores.

![Color gird]()

### **Typography**:

# **Building Process Process**
  Using a Kanban Board system. And Something similar to sprints. 

  When it came to actually putting my Database Schema into reality a few things changed. Such as Saved and Categories. Plus I figured out I would need to make a model purely for the rating system I wanted to put in place. MVP this could just be likes, but to differentiate from the base of this project (which was taken from Code Insitutes 'Django Blog App') I wanted to add in this rating system that would calculate a recipes' popularity. This would also be the building block of the carousels on the recipe search page. I plan to have 'Diet' and even 'In Season' Caraousels on the recipe search page so that site users can easily see recipes, the rating system will determine which recipes show up on these carousels. Or So I Plan... (Famous last words of a coder).
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
* For Django Models resources I used [Geeks For Geeks: Django Model](https://www.geeksforgeeks.org/django-models/?ref=lbp)
   
