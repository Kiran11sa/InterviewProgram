*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.opencart.com/

*** Test Cases ***
TestingInputbox
    open browser   ${url}  ${browser}
    maximize browser window
    title should be  Your Store
#    title should not be   Your Stor
    click element  xpath://span[normalize-space()='My Account']
    click element    link:Login
    ${"email"}   set variable    id:input-email
    element should be visible   ${"email"}
    element should be enabled    ${"email"}
    clear element text    ${"email"}
    sleep  4s
    input text   ${"email"}     kirankodigela@gmail.com
