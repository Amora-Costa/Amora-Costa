console.log('hello')

function navBtnClicked (){
    const nav = document.getElementById('header-div-two')

    const navBtn = document.getElementById('nav-btn')

    nav.style.display = 'flex'
    navBtn.style.display = 'none'
}

function navClose(){
    const close = document.getElementById('close-btn')
    const navBtn = document.getElementById('nav-btn')
    const nav = document.getElementById('header-div-two')

    nav.style.display = 'none'
    navBtn.style.display = 'block'

}

function showSucess() {
    const story1 = document.getElementById('sucess-group-1');
    const story2 = document.getElementById('sucess-group-2');
    const story3 = document.getElementById('sucess-group-3');
    const section1 = document.getElementById('section-one');
    const section2 = document.getElementById('section-2');
    const section3=document.getElementById('section-3')
    let step = 0;

    function cycleStories() {
        // Hide all stories
        story1.style.display = "none";
        story2.style.display = "none";
        story3.style.display = "none";

        // Hide both sections by default
        section1.style.display = 'none';
        section2.style.display = 'none';
        section3.style.display = 'none';

        // Display content based on step
        switch (step % 3) {
            case 0:
                story1.style.display = "flex";
                section1.style.display = 'flex';
                break;
            case 1:
                story2.style.display = "flex";
                section2.style.display = 'flex';
                break;
            case 2:
                story3.style.display = "flex";
                section3.style.display = 'flex';
                break;
        }

        step++;
        setTimeout(cycleStories, 10000); // Repeat every 10 seconds
    }

    cycleStories(); // Start the loop
}

showSucess()
    

function openPop(){
    const pop = document.getElementById('pop-up-form-div');
  




    pop.style.display = 'flex'
    
}
function closePop(){
    const pop = document.getElementById('pop-up-form-div')
  


    pop.style.display = 'none'
}

function openPrivacy(){
    const privacy = document.getElementById('privacy-inner')
    const open = document.getElementById('privacy-open')
    const close = document.getElementById('privacy-close')


    privacy.style.display = "flex"
    privacy.style.flexDirection = "column"
    open.style.display = "none"
    close.style.display = "flex"
}

function closePrivacy(){
    const privacy = document.getElementById('privacy-inner')
    const open = document.getElementById('privacy-open')
    const close = document.getElementById('privacy-close')

    privacy.style.display = "none"
    open.style.display = 'inline'
    close.style.display = "none"
}