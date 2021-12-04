const signupForm = document.getElementById('signup-form');

signupForm.onsubmit=(e) => handleSignup(e);

const handleSignup = (e) => {
    e.preventDefault();
    username = getUsername();
    passwords = getPassword();
    console.log(`사용자 이름: ${username}`);
    if(validateUsername(username) && validatePassword(passwords)){
        console.log('valid signup form!')
        submitTarget(e);
    } else {
        console.log('Invalid!')
        console.log(errorModal.classList)
        dismissSignup();
        setGrayBackGroundColor();
    }
};

const modalCloseBtn = document.querySelector('.modal-header > .close-button');
modalCloseBtn.onclick = () => handleClose();

const handleClose = () => {
	hideErrorModal();
    resetGrayBackGroundColor();
};

const bodyTag = document.querySelector('body');

const setGrayBackGroundColor = () => {
	bodyTag.classList.add('gray');
};

const resetGrayBackGroundColor = () => {
	bodyTag.classList.remove('gray');
};

const hideErrorModal = () => {
	errorModal.classList.remove('show');
}

const dismissSignup = () => {
    showErrorModal();
}
const errorModal = document.getElementById('signup-error-modal');
const showErrorModal = () => {
	errorModal.classList.add('show');
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
	return isSamePassword(passwords) && isValidFormatPassword(passwords) ;
};

const isValidFormatPassword = ([pw]) => {
	const regExp = /^[A-Za-z0-9]{3,}$/;

	return regExp.test(pw);
};

const isSamePassword = ([pw1, pw2]) => {
	return pw1 === pw2;
};

const submitTarget = (e) => {
    e.target.submit();
};
