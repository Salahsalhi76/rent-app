import { useEffect, useState } from 'react';
import './App.css';
import jwtDecode from 'jwt-decode';

function App() {
  const [user, setUser] = useState({});
  
  function handleCallBackResponse(response){
    console.log("Encoded JWT ID token: " + response.credential);
    var userObject = jwtDecode(response.credential);
    console.log(userObject)
    setUser(userObject);
    document.getElementById("signInDiv").hidden = true;
  } 

  function handleSingOut(event){
    setUser({});
    document.getElementById("signInDiv").hidden = false;
  }

  useEffect(()=>{ 
   /* globle google */ 
    google.accounts.id.initialize({
      client_id: "701297576119-3v2p4bf25tevk283ejpl1le48lctlo63.apps.googleusercontent.com",
      callback: handleCallBackResponse
    });

    google.accounts.id.renderButton(
      document.getElementById("signInDiv"),
      { theme: "outline", size: "medium"}
    )
    /*google.accounts.id.prompt();*/
  }, []);

  return (
    <div className="App-a">
      <div id="signInDiv"></div>
      {Object.keys(user).length != 0 &&
        <button onClick={(e) => handleSingOut(e)}>Sign Out</button>
      }
      {user &&
        <div>
          <img src={user.picture}></img>
          <h3> {user.name} </h3>
        </div>
      } 
    </div>
  );
}

export default App;



// import { useEffect, useState } from 'react';
// import './App.css';
// import jwtDecode from 'jwt-decode';

// function App() {
//   const [user, setUser] = useState({});
  
//   function handleCallBackResponse(response){
//     console.log("Encoded JWT ID token: " + response.credential);
//     var userObject = jwtDecode(response.credential);
//     console.log(userObject)
//     setUser(userObject);
//     document.getElementById("signInDiv").hidden = true;
//   }

//   function handleSingOut(event){
//     setUser({});
//     document.getElementById("signInDiv").hidden = false;
//   }

//   useEffect(()=>{ 
//    /* globle google */ 
//     google.accounts.id.initialize({
//       client_id: "701297576119-3v2p4bf25tevk283ejpl1le48lctlo63.apps.googleusercontent.com",
//       callback: handleCallBackResponse
//     });

//     google.accounts.id.renderButton(
//       document.getElementById("signInDiv"),
//       { theme: "outline", size: "medium"}
//     )
//     /*google.accounts.id.prompt();*/
//   }, []);

//   return (
//     <div className="App">
//       <div id= "signInDiv"></div>
//       {Object.keys(user).length != 0 &&
//        <button onClick={(e) => handleSingOut(e)}>Sign Out</button>
//       }
//       { user &&
//         <div>
//           <img src={user.picture}></img>
//           <h3> {user.name} </h3>
//         </div>
//       }
//     </div>
//   );
// }

// export default App;

