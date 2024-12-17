*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://artoftesting.com/samplesiteforselenium

*** Test Cases ***
dropdown
    open browser   ${url}  ${browser}
    maximize browser window
    select from list by value   Drop down     automation

#    sleep  4s
#    Select From List By Label    Drop down     Performance

    sleep  4s