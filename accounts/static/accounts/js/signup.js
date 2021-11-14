const signupForm = document.getElementById('signup-form');

signupForm.onsubmit=(e) => handleSignup(e);

const handleSignup = (e) => {
    e.preventDefault();
    username = getUsername();
    passwords = getPassword();
    console.log(`사용자 이름: ${username}`);
    if(validateUsername(username) && validatePassword(passwords)){
        console.log('valid signup form!')
    } else {
        console.log('Invalid!')
    }
};

const getUsername = () => {
    return document.querySelector('input[name=username]').value;
}

const validateUsername = (username) => {
	return username !== '';
};

const getPassword = () => {
    return [...document.querySelectorAll('input[type=password]')].map(
        (input) => input.value
    )
}

const validatePassword = (passwords) => {
	return isSamePassword(passwords);
};

const isSamePassword = ([pw1, pw2]) => {
	return pw1 === pw2;
};

