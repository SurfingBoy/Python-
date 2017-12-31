import builtwith
import whois
print('网站所用技术:',builtwith.parse('http://www.runoob.com')) #网站所用技术
print('网站拥有者:',whois.whois('http://www.runoob.com'))     #网站拥有者
