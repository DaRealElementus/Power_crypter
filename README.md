<span style="color:red">Due to unrestricted ASCII code, data loss may happen</span>.
# Power_crypter
Funky python Vigenère cypher (but dumb)
also avaliable on [Replit](https://replit.com/@ItsmeElementus/PowerCrypter?v=1)

# Required modules
colorama - installed with pip through cmd - C:\>``` pip install colorama ```
ensure that you have setup pip before installing

# How does it work?
This progarm takes your key `(12345.....)` and turns it into `[1], [2], [3], [4], [5].....`<br>
It then takes your phrase `(Hello)` and turns it into `[H], [e], [l], [l], [o]`<br>
It then rotates your phrase by what number coresponds to the character<br>
```
H   e   l   l   o
1   2   3   4   5
^   ^   ^   ^   ^
L   n   q   l   t
```
