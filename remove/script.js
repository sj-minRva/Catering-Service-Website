function sendMail(){
    let parms={
        
        name : document.getElementById("name").value.trim(),
        email : document.getElementById("email").value.trim()
    }

    emailjs.send("service_pb250zp","template_nna63fa",parms).then(alert("Email Sent"))
}