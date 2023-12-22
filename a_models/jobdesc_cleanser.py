
def clean_please(text):
    # ----------------------------------------------------------    
    text = text.replace('"html":', '')
    text = text.replace('<li style="margin-left:30px">', '|')  
    text = text.replace('<li style="text-align:justify">', '|')  
    text = text.replace('u002F', '/')
    text = text.replace('u003C', '<')
    text = text.replace('u003E', '>')
    # ----------------------------------------------------------    
    text = text.replace('</p>', '|')
    text = text.replace('<p>', '')
    # ----------------------------------------------------------    
    text = text.replace('</b>', '|')
    text = text.replace('<b>', '|')
    # ----------------------------------------------------------    
    text = text.replace('</strong>', '|')
    text = text.replace('<strong>', '|')
    # ----------------------------------------------------------     
    text = text.replace('</li>', '|')
    text = text.replace('<li>', '|')
    # ----------------------------------------------------------    
    text = text.replace('</ol>', '|')
    text = text.replace('<ol>', '|')
    # ----------------------------------------------------------    
    text = text.replace('</ul>', '|')
    text = text.replace('<ul>', '|')
    # ----------------------------------------------------------    
    text = text.replace('</u>', '|')
    text = text.replace('<u>', '|')
    # ----------------------------------------------------------    
    text = text.replace('</em>', '|')
    text = text.replace('<em>', '|')
    # ----------------------------------------------------------    
    text = text.replace('</div>', '|')
    text = text.replace('<div>', '|')
    # ----------------------------------------------------------    
    text = text.replace('<br />', '|')
    # ----------------------------------------------------------    
    text = text.replace('          ', '')  
    text = text.replace('             ', '') 
    text = text.replace('        ', '') 
    text = text.replace(' ', '') 
    # ----------------------------------------------------------
    text = text.replace('•', '') 
    text = text.replace('&amp;', '&') 
    text = text.replace('&lt;', '') 
    text = text.replace('&gt;', '')  
    # ----------------------------------------------------------   
    text = text.replace(' –', '–')  
    text = text.replace('– ', '–')  
    text = text.replace('–', ' – ')  
    # ---------------------------------------------------------- 
    text = text.replace('﻿', '')   
    text = text.replace('​', '')   
    # ----------------------------------------------------------   
    text = text.replace(' (', '(')  
    text = text.replace('( ', '(')  
    text = text.replace('(', ' ( ')  
    # ----------------------------------------------------------   
    text = text.replace(') ', ')')  
    text = text.replace(' )', ')')  
    text = text.replace(')', ' ) ')  
    # ----------------------------------------------------------   
    text = text.replace('. ', '.')  
    text = text.replace(' .', '.')  
    text = text.replace('.', ' . |')  
    # ----------------------------------------------------------   
    text = text.replace(', ', ',')  
    text = text.replace(' ,', ',')  
    text = text.replace(',', ' , ')  
    # ----------------------------------------------------------   
    text = text.replace('/ ', '/')  
    text = text.replace(' /', '/')  
    text = text.replace('/', ' / ')  
    # ----------------------------------------------------------   
    text = text.replace('- ', '-')  
    text = text.replace(' -', '-')  
    text = text.replace('-', ' - ')  
    # ----------------------------------------------------------   
    text = text.replace(': ', ':')  
    text = text.replace(' :', ':')  
    text = text.replace(':', ' : ')  
    # ----------------------------------------------------------   
    text = text.replace('? ', '?')  
    text = text.replace(' ?', '?')  
    text = text.replace('?', ' ? ')  
    # ----------------------------------------------------------   
    text = text.replace('! ', '!')  
    text = text.replace(' !', '!')  
    text = text.replace('!', ' ! ')  
    # ----------------------------------------------------------   
    text = text.replace('+ ', '+')  
    text = text.replace(' +', '+')  
    text = text.replace('+', ' + ')  
    # ----------------------------------------------------------   
    text = text.replace('# ', '#')  
    text = text.replace(' #', '#')  
    text = text.replace('#', ' # ')  
    # ----------------------------------------------------------   
    text = text.replace('; ', ';')  
    text = text.replace(' ;', ';')  
    text = text.replace(';', ' ; ')  
    # ----------------------------------------------------------   
    text = text.replace('* ', '*')  
    text = text.replace(' *', '*')  
    text = text.replace('*', ' * ')  
    # ----------------------------------------------------------   
    # text = text.replace('\ ', '\')  
    # text = text.replace(' \', '\')  
    text = text.replace("\\", "")
    # ---------------------------------------------------------- 
    text = text.replace('·', '')  
    text = text.replace('"', '')  
    # ---------------------------------------------------------- 
    text = text.replace('<li style=margin - left : 30px>', '|')  
    text = text.replace('<li style=text - align : justify>', '|')  
    
    text = text.replace('<div style=text - align : justify>', '|')   
    text = text.replace('<p style=margin - left : 90px>', '|')   
    text = text.replace('<p style=margin - left : 60px>', '|')   
    
    #  
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, " ", "")
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, " ", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "⭐ ", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "⭐️ ", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "➕ ", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "❗", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "✅", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "⚫ ", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "⚙️ ", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "⏰", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=margin - left : 30px>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=margin - left : 150px>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "< / b>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<b>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=margin - left : 120px>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=margin - left : 180px>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<li style=margin - left : 60px>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=color : rgb ( 28 , 28 , 28 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=color : rgb ( 28 , 28 , 28 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<span style=color : rgb ( 28 , 28 , 28 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "< / span>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<span>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=color : rgb ( 51 , 51 , 51 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=color : rgb ( 0 , 0 , 0 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=color : rgb ( 20 , 42 , 91 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=color : rgb ( 51 , 62 , 73 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<span style=color : rgb ( 20 , 42 , 91 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<p style=color : rgb ( 102 , 102 , 102 ) ; text - align : justify>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=color : rgb ( 121 , 123 , 124 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=text - align : left>", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "<div style=color : rgb ( 32 , 35 , 37 ) >", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "	", "");
    # UPDATE `jobdescription_dataset` SET `name` = REPLACE(`name`, "        ", "");
    
    # ---------------------------------------------------------- 
    text = text.replace('  ', ' ')    
    # ---------------------------------------------------------- 
    return text
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
    # ----------------------------------------------------------   
