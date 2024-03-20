# Burp Suite

Burp Suite is a set of tools for web application security testing.

First and foremost, use the button `open browser` to open a browser that is configured to use Burp Suite as a proxy.

## Decoder

Decoder is a tool that can be used to decode/encode data. It is a very useful tool for web application security testing.

![decoder](assets/decoder.png)

In this example we encoded a string into base64.

## Repeater

Repeater is a tool that can be used to repeat requests. Specially usefull when want to do crafted payloads.

![repeater](assets/repeater_1.png)

While you are here, you can click on a request then CTRL+R to send it to the repeater. or second click on the request and select `Send to Repeater`.

![repeater](assets/repeater_2.png)

And here we can modify the request and send it again.

## Proxy

### Intercept

We can use the intercept to capture requests and save them to a file.

![intercept](assets/intercept.png)         

Here if we do right click and press `Copy to file` we can save the request to a file.                                       