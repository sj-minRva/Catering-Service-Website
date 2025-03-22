function sendMail(){
    let parms={
        subject : document.getElementById("subject").value,
        name : document.getElementById("name").value,
    }

    emailjs.send("service_pb250zp","template_s4j9xkd",parms).then(alert("Email Sent"))
}