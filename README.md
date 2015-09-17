#Subterfuge

Branch development of a Subterfuge more GIT resident is ongoing for the latest details see: http://kinozoa.com/blog/development/

##Installation

Follow the steps below to download and install the latest version of Subterfuge:
```
git clone https://github.com/Subterfuge-Framework/Subterfuge.git
cd Subterfuge
python setup.py
```

Execute Subterfuge by running the following command:
```
subterfuge
```

##Subterfuge – 2015

Where oh where did all of the progress go!?!? As the development team has gone off in many directions we’ve had to restructure our project goals and timeline. Subterfuge isn’t dead, but we certainly changed the way we do business. Here’s the short and sweet of it:

###– What happened to updates: SVN is dead long live .DEB… .DEB is dead long live GIT

When Google Code fell apart a couple years ago we had to scramble to change the way we provided updates and pushed new content. Due to miscommunication with the Kali Linux dev team we moved to the Debian packaging system more colloquially known as apt. Unfortunately, this change almost killed the whole project by completely severing our ability to provide updates to the framework.

In effect this means that old versions of Subterfuge CANNOT receive updates! We’re moving to GitHub. Once that process is complete you’ll be able to download a new version of the framework capable of receiving new content.

###– What have you done for me lately!

It looks like many folks missed our March 2015 Subterfuge update. We wanted to start the year off with a bang re-energizing the framework by extending it with new attack options: Subterfuge version 1.0.1. Here’s a breakdown of the new functionality we’ve pushed out in 2015.

*Subterfuge can now MITM SSL sessions using arbitrary certificates
*SSLStriping can be selectively enabled or disabled as desired
*Subterfuge can leverage the Superfish Bug
*CRITICAL UPDATE: The new version of Django was causing Subterfuge to fail on default installs of Kali Linux. Subterfuge 1.0.1 release with emergency fixes to critical framework files.

###– In the pipe 5 by 5

We have BIG plans for Subterfuge 2015 development, but we don’t know exactly when we’ll be able to put out new content or fix existing stability issues. Our transition to GitHub might be a great opportunity for you to get involved. Don’t hesitate to send me an email if you’re interested. See our project roadmap below for more details on the 2015 development plan.

##Subterfuge Development Roadmap 2015

In this section we’ll detail out major feature and stability modifications to Subterfuge by version as they are released. We will then finish with a listing of future development goals and (VERY ROUGH) projections regarding release.

##Version 1.0.1 – Superfish!

*Subterfuge can now MITM SSL sessions using arbitrary certificates
*SSLStriping can be selectively enabled or disabled as desired
*Subterfuge can leverage the Superfish Bug
*CRITICAL UPDATE: The new version of Django was causing Subterfuge to fail on default installs of Kali Linux. Subterfuge 1.0.1 release with emergency fixes to critical framework files
*Next Expected Release – Version 2.0 – October 2015

##Upcoming Content

Transition to GitHub
POODLE Exploit Module
Heartbleed Module
SSL v3 Downgrade Module


##Summary:

Walk into Starbucks, plop down a laptop, click start, watch the credentials roll in. Enter Subterfuge, a Framework to take the arcane art of Man-in-the-Middle Attack and make it as simple as point and shoot. A beautiful, easy to use interface which produces a more transparent and effective attack is what sets Subterfuge apart from other attack tools. Subterfuge demonstrates vulnerabilities in the ARP Protocol by harvesting credentials that go across the network, and even exploiting machines through race conditions. Now walk into a corporation…

A rapidly-expanding portion of today’s Internet strives to increase personal efficiency by turning tedious or complex processes into a framework which provides instantaneous results. On the contrary, much of the information security community still finds itself performing manual, complicated tasks to administer and protect their computer networks. Given the increase in automated hacking tools, it is surprising that a simplistic, “push-button” tool has not been created for information security professionals to validate their networks’ ability to protect against a Man-In-The-Middle attack. Subterfuge is a small but devastatingly effective credential-harvesting program which exploits a vulnerability in the Address Resolution Protocol. It does this in a way that a non-technical user would have the ability, at the push of a button, to harvest all of the usernames and passwords of victims on their connected network, thus equipping information and network security professionals with a “push-button” security validation tool.


