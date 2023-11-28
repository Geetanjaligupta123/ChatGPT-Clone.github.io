
    
    // Example POST method implementation:
async function postData(url = "", data = {}) {
   
    const response = await fetch(url, {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      
      
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
/////////////////
sendButton.addEventListener("click",async ()=>{
    alert("Hey you clicked");
    questionInput = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value="";
    document.querySelector(".right2").style.display = "block";
    document.querySelector(".right1").style.display = "none";

    question1.innerHTML=questionInput;
    question2.innerHTML=questionInput;


    //
   let result =  await postData("/api",{"question":"questionInput"})
    solution.innerHTML = result.result;

} )