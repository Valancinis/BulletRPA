# BulletRPA
#### Video Demo:  <https://youtu.be/FnMiUqZV1xI>
#### Description:
This is the description for CS50 course. This project is a UI for custom RPA bots that my RPA business will use. I have built a UI software for managing and scheduling RPA robots. Curently I am building various bots for my customers and I wanted to have a custom software so my customers could manage their bots easily.

Current Bullet-RPA itteration allows users to add bots, they are saved to the json file which is stored localy on users computers. Then users are allowed to launch bot manually or shedule their bots to run periodidally. Users can put in time interval for how offten they want their bot to run and bots will run as long as Bullet-RPA is running.

User can also delete bots if they no longer need them.

Design choices:
My fail contains a generic software structure. All the main UI elements, functions and code is in main.py as it is easyer to work with flets control elements if they are int he same file. There are couple additional files that are used in main.py. There is workers.py and helpers.py that handle various functions that do not need to be in main.py. There also is robots.json file that stores data for each bot that are added. Finally there are few files with classes that I was building, I no longer use them due to how flets column scroll functionality react to labda functions inside of controlls, but I kept them in case I will need them ever again.

This code is build with Flet for cross-platform capabilities of this framework.

Enhanced User Experience:
Intuitive Interface: The UI is designed to be user-friendly and straightforward, ensuring that even users with minimal technical expertise can easily manage their bots.
Real-time Feedback: Users receive immediate visual feedback on the status of their bots, including success, failure, and execution logs.
Customizable Settings: Offers flexibility in scheduling, allowing for precise timing and frequency adjustments to suit various business needs.
Security Measures:
Local Data Storage: All data related to bots, including scheduling and script information, is stored locally, ensuring data privacy and security.
Robust Error Handling: The application is equipped with comprehensive error handling to prevent crashes and ensure smooth operation.

#### Plans after CS50 (And the original description)
Here is a repository for "Bullet", an RPA software. We are building an easy to use RPA software that with only few steps allow users to automate basic data copy/pasting actions for lists of data.

The initial steps of this software is to have an interface that allows our clients to access their RPA bots easily, to add/remove robots, schedule their run time and choose what to do when robots stop running.

The next step is to have an automation capability built in to the "Bullet-RPA" interface, where users could very quickly set up a few step robot that does up to 10 steps and then loops those steps for another iteration or another object. This functionality will eliminate tasks that are not mundane, but might take few hours to do every time you face such task.

#### USAGE
This is a private project, to use it, you must contact developing team, ask for a demo and for a setup.

FUTURE FEATURES
- Storing your .exe .bat and other file type scripts/robots in a single interface, that allows you to control those robots, schedule them easily and launch robots on startup.
- Up to 10 step cycle automation for unique manual labor task automation.

#### CONTRIBUTING
We welcome contributions and suggestions for improvements. Please feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
Ensure to update tests as appropriate and adhere to the existing coding standards.
LICENSE
This project is licensed under [appropriate license], allowing for redistribution and use in source and binary forms, with or without modification.
