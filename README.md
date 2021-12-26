# Onscreen Checklist Documentation 📝
This project mainly uses PyQt5 with custom functions to faciliate a checklist. The GUI is set on the topmost layer of all applications, meaning it will constantly be seen despite changing applications.

## 🎄 Installation
- As of v1.0.0, installation is unavailable.

## 🔻 Usage
Running the Onscreen Checklist Program will present the following UI on the left-hand side of the screen...  

![image](https://user-images.githubusercontent.com/58658294/147415765-afcf1609-2e76-4b38-bf61-91677db6afe4.png)

- As can be seen, it is a GUI on the left of the screen with **an "ADD" button**, **a "REMOVE" button** (initially disabled), **a minimize toggle button**, **an exit button**, and a "sort by" **drop-down list**.
- NOTE: The "sort by" drop-down list does not currently have any functionalities in version 1.0.0
  
  ### Adding an Item ➕
 - In clicking the "ADD" button, a second UI will appear right below the main one where a user can add in a To-Do Item by inputting a title, a description/extra information, and the importance rating.   
 ![image](https://user-images.githubusercontent.com/58658294/147415909-3047a63e-6527-42db-940f-1f497a6ba8df.png)
- The user may then press "DONE" to add the item to the to do-list.  
 ![image](https://user-images.githubusercontent.com/58658294/147415936-2d4fc6a2-fa85-4c76-9c29-1cf899ee4e32.png)

### Clicking an Item 🖱️
- Once an item exists in the to-do list, clicking on any item will now display the item's description along with the importance level set by the user. The "REMOVE" button will also now be available for use.  
![image](https://user-images.githubusercontent.com/58658294/147415988-70e929f1-67e1-4903-b560-54149b713d63.png)

### Minimizing the GUI ➖
- To minimize the GUI, the minimize button on the main GUI should be clicked. 
- Once the button has been clicked, the GUI will minimize and will appear as a blue bar on the left-hand side of the screen such as follows...  
![image](https://user-images.githubusercontent.com/58658294/147416038-7d4f4e2f-9ec9-4bbf-bd90-f0a400a49874.png)
- Clicking on the bar will open the GUI once more with previous information intact.

### Roadmap 🚀
- [ ] Create dark mode / allow for a variety of color palettes.
- [ ] Improve to-do item display in the main GUI.
- [ ] Allow users to input the date/time to accomplish the to-do item by as an optional feature.
- [ ] Allow users to sort by a to-do list's importance / date.
- [ ] Implement an easy way to install / use the program.
