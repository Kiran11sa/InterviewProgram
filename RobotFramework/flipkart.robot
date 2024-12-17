*** Settings ***
Library  SeleniumLibrary






*** Variables ***
${browser}      chrome
${url}      https://www.flipkart.com/

*** Test Cases ***
searchinflipkart
       open browser   ${url}    ${browser}

       click link    xpath://a[@aria-label='Electronics']//div[@class='_2GaeWJ']



*** Keywords ***


