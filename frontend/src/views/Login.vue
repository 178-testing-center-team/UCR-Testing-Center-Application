<template>
    <div class="login">
        <h1 class="login-welcome"><b>Welcome to the UCR Testing Center</b></h1>
        <p class="login-trouble">Trouble Connecting?<br>Contact us at: sendhelp@ucr.edu</p>


    <div class=login-box><span  class="login-box-title">Login</span>
    <div class="user-shape"></div><span  class="us-text">username...</span>
    <div class="pass-shape"></div><span  class="pass-text">password...</span><span  class="forgot-pass">Forgot your password? Click here</span>
    <div class="sign-in-button"></div><span  class="sign-in-text">SIGN IN</span>
    </div>


    </div>



</template>



<style>
.login {
    background-image: url('../assets/imgs/loginBackground.svg');
    background-repeat: no-repeat;
    background-position-x: center;
    background-position-y: center;
    background-size: contain;
    background-color: black;
    height: 100vh;
    width: auto;
}

.login-box { 
	box-shadow:0px 4px 4px rgba(0, 0, 0, 0.25);
	background-color:rgba(25.000000409781933, 27.000000290572643, 30.00000011175871, 0.75);
	width:583px;
	height:389px;
    display: inline-block;
    text-align: center;
    justify-content: center;
    transform: translate(0, 50%);

}
	
.login-box-title { 
	color:rgba(255, 255, 255, 1);
	width:93px;
	height:71px;
	position:absolute;
	left:66px;
	top:4px;
	font-family:Oswald;
	text-align:center;
	font-size:48px;
	letter-spacing:0;
}
.user-shape { 
	background-color:rgba(217.0000022649765, 217.0000022649765, 217.0000022649765, 1);
	width:422px;
	height:70px;
	position:absolute;
	left:81px;
	top:100px;
	border-top-left-radius:108px;
	border-top-right-radius:108px;
	border-bottom-left-radius:108px;
	border-bottom-right-radius:108px;
}
.us-text { 
	color:rgba(0, 0, 0, 1);
	width:131px;
	height:47px;
	position:absolute;
	left:112px;
	top:109px;
	font-family:Oswald;
	text-align:left;
	font-size:32px;
	letter-spacing:0;
}
.pass-shape { 
	background-color:rgba(217.0000022649765, 217.0000022649765, 217.0000022649765, 1);
	width:422px;
	height:70px;
	position:absolute;
	left:81px;
	top:195px;
	border-top-left-radius:108px;
	border-top-right-radius:108px;
	border-bottom-left-radius:108px;
	border-bottom-right-radius:108px;
}
.pass-text { 
	color:rgba(0, 0, 0, 1);
	width:133px;
	height:47px;
	position:absolute;
	left:112px;
	top:205px;
	text-align:left;
	font-size:32px;
	letter-spacing:0;
}
.forgot-pass { 
	color:rgba(255, 255, 255, 1);
	width:487px;
	height:38px;
	position:absolute;
	left:48px;
	top:345px;
	font-family:Inria Serif;
	text-align:center;
	font-size:32px;
	letter-spacing:0;
}
.sign-in-button { 
	background-color:rgba(249.00000035762787, 193.00000369548798, 68.00000354647636, 1);
	width:185px;
	height:58px;
	position:absolute;
	left:199px;
	top:281px;
    justify-content: center;
	border-top-left-radius:30px;
	border-top-right-radius:30px;
	border-bottom-left-radius:30px;
	border-bottom-right-radius:30px;
}
.sign-in-text { 
	color:rgba(60.957400649785995, 61.25533506274223, 61.62499822676182, 1);
	width:99px;
	height:30px;
	position:absolute;
	left:242px;
	top:295px;
	font-family:Oswald;
	text-align:left;
	font-size:26px;
	letter-spacing:0;
}
</style>



