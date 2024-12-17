*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://artoftesting.com/samplesiteforselenium

*** Test Cases ***
TRadioandcheck
    open browser   ${url}  ${browser}
    maximize browser window
    select radio button    gender   male

    sleep   4s
    select checkbox    Automation
    select checkbox      Performance

    unselect checkbox        Performance

    sleep  5s