## Sherlock Scenario

Simon, a developer working at Forela, notified the CERT team about a note that appeared on his desktop. The note claimed that his system had been compromised and that sensitive data from Simon's workstation had been collected. The perpetrators performed data extortion on his workstation and are now threatening to release the data on the dark web unless their demands are met. Simon's workstation contained multiple sensitive files, including planned software projects, internal development plans, and application codebases. The threat intelligence team believes that the threat actor made some mistakes, but they have not found any way to contact the threat actors. The company's stakeholders are insisting that this incident be resolved and all sensitive data be recovered. They demand that under no circumstances should the data be leaked. As our junior security analyst, you have been assigned a specific type of DFIR (Digital Forensics and Incident Response) investigation in this case. The CERT lead, after triaging the workstation, has provided you with only the Notepad++ artifacts, suspecting that the attacker created the extortion note and conducted other activities with hands-on keyboard access. Your duty is to determine how the attack occurred and find a way to contact the threat actors, as they accidentally locked out their own contact information. Warning : This sherlock requires an element of OSINT and players will need to interact with 3rd party services on internet.

1. What is the full path of the script used by Simon for AWS operations?

Inside the `config.yml` file line 9 there is the path 

`<File filename="C:\Users\Simon.stark\Documents\Dev_Ops\AWS_objects migration.pl" />`

2. The attacker duplicated some program code and compiled it on the system, knowing that the victim was a software engineer and had all the necessary utilities. They did this to blend into the environment and didn't bring any of their tools. This code gathered sensitive data and prepared it for exfiltration. What is the full path of the program's source file?

Inside the `session.yml` file line 5 there is both the source and backup path

`filename="C:\Users\Simon.stark\Desktop\LootAndPurge.java" backupFilePath="C:\Users\Simon.stark\AppData\Roaming\Notepad++\backup\LootAndPurge.java@2023-07-24_145332"`

3. What's the name of the final archive file containing all the data to be exfiltrated?

Inside the LootAndPurge.java file there is a line that contains the name of the file

```java
zipOutputStream.setComment("Forela-Dev-Data.zip");
```

So our response is `Forela-Dev-Data.zip`

4. What's the timestamp in UTC when attacker last modified the program source file?

`2023-07-24 09:53:23`

5. The attacker wrote a data extortion note after exfiltrating data. What is the crypto wallet address to which attackers demanded payment?

Inside the `LootAndPurge.java` file there is the password

```java
String password = "sdklY57BLghvyh5FJ#fion_7";
```

There we can go into

https://pastebin.com/CwhBVzPq	

OR 

https://pastes.io/mvc6sue6cf	

Paste the password there and we will get the response

`0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca`

6. What's the email address of the person to contact for support?

From the previous point we also get the email address

`CyberJunkie@mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion`