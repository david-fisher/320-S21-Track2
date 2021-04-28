import React, { useEffect } from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  Button,
  makeStyles,
} from "@material-ui/core";
import { BASE_URL, STUDENT_ID, SCENARIO_ID }from "../constants/config";
import SubmitButton from "./components/Buttons/SubmitButton"
import TextField from '@material-ui/core/TextField';
import axios from "axios";


const TextTypography = withStyles({
  root: {
    color: "#373a3c",
    whiteSpace: "pre-wrap",
  },
})(Typography);


const useStyles = makeStyles((theme) => ({
  textBox: {
    overflowY: "auto",
    maxHeight: window.innerHeight * 0.6,
    marginTop: theme.spacing(4),
    borderRadius: "5px",
    boxShadow: "0px 0px 2px",
  },
}));

function  Reflection(props){
  const [name, setName] = React.useState("");
  const [data, setData] = React.useState("");
  function  handleResponse(data){
    const items = {
      response: 1,
      student: String(STUDENT_ID),
      scenario: SCENARIO_ID,
      version:2,
      page:props.id,
      course: 1,
      choice:'none',
      reflection:data
    };
    axios.post(BASE_URL + `/reflection_response/?page_id=${props.id}&student_id=${STUDENT_ID}&scenario_id=${SCENARIO_ID} `,items)
    .then(response=>console.log(response.data.reflections))
    .catch(e=>{console.log(e)})
   }
   const handleChange = (event) => {
    setName(event.target.value);
  };
  const classes = useStyles();
  
  useEffect(()=>{
    fetch(BASE_URL + `/reflection_response/?page_id=${props.id}&student_id=${STUDENT_ID}&scenario_id=${SCENARIO_ID} `)
    .then(response=>response.json())
    .then(data=> setData(data.reflections))
  })
  return(
    <div>
    <Box mt={5}>
      <Grid container direction="row" justify="center" alignItems="center">
        <TextTypography variant="h4" align="center" gutterBottom>
          {props.title}
        </TextTypography>
      </Grid>
        <Grid container spacing={2}>
         <Grid item lg={12}>
           <Box m="2rem">
           </Box>
           <Box p={2} className={classes.textBox}>
           <TextTypography variant="body1" paragraph = {true} gutterBottom>
             {props.content}
          </TextTypography>
          </Box>
         </Grid>
       </Grid>
       <Grid container spacing={2}>
         <Grid item lg={12}>
           <Box m="2rem">
           </Box>
           <Typography variant="body1" paragraph = {true} gutterBottom>
              <TextField
                required
                fullWidth
                defaultValue = {data}
                multiline = {true}
                autoComplete = "off"
                id="filled-required"
                label="Required"
                variant="filled"
                onChange = {handleChange}
                InputLabelProps = {{shrink:true}}
              />
              <Box pt={2}>
                <SubmitButton title = "submit" onClick={() => handleResponse(name)}/>
              </Box>
          </Typography>
         </Grid>
       </Grid>
    </Box>
    </div>
  );
}
export default Reflection;

// function Reflection({ pages, setPages, activePage, setActivePage,
//   content_url, res_url, nextPageID, prevPageID , title}) {

//   function goToPage(pageID) {
//     if (pages[pageID].completed) {
//       if (!pages[pageID].visited) {
//         setPages((prevPages) => {
//           let copy = { ...prevPages };
//           copy[pageID].visited = true;
//           return copy;
//         });
//       }
//       setActivePage((prevPage) => pageID);
//     }
//   }

//   let prevPageTitle;
//   const classes = useStyles();

//   const [bodyText, setBodyText] = React.useState('');
//   const [prompts, setPrompts] = React.useState([]);
//   const [promptResponses, setPromptResponses] = React.useState({});
//   const [scenarios, setScenarios] = React.useContext(ScenariosContext);

//   React.useEffect(() => {
//     (async () => {
//       await axios({
//         method: 'get',
//         url: BASE_URL + content_url,
//         headers: {
//           scenarioID: scenarios.currentScenarioID
//         }
//       }).then(response => {
//         setBodyText(response.data.body_text);
//         setPrompts(prev => response.data.prompts);
//       }).catch(err => {
//         console.log(err);
//         alert(err);
//       });

//       axios({
//         method: 'get',
//         url: BASE_URL + res_url,
//         headers: {
//           scenarioID: scenarios.currentScenarioID,
//           studentID: STUDENT_ID
//         }
//       }).then(response => {
//         setPromptResponses(response.data.reduce((prev, curr) => {
//           prev[curr.prompt_num] = curr.response;
//           return prev;
//         }, {}));
//       }).catch(err => {
//         console.log(err);
//       });
//     })();
//   }, [scenarios, activePage]);

//   async function handleResponse(data) {
//     await axios({
//       url: BASE_URL + content_url,
//       method: 'put',
//       data: {
//         scenarioID: scenarios.currentScenarioID,
//         studentID: STUDENT_ID,
//         data: data
//       }
//     });
//   }

//   function getPrevPageTitle(prevPageID) {
//     switch (prevPageID) {
//       case "projectAssignment": prevPageTitle = "Project Assignment";
//       break;
//       case "stakeholders": prevPageTitle = "Stakeholders";
//       break;
//       case "feedback": prevPageTitle = "Feedback";
//       break;
//       default:
//         break;
//     }
//   }

//   getPrevPageTitle(prevPageID);

//   return (
    
    // <div>
    //   <Grid container direction="row" justify="center" alignItems="center" noWrap={true}>
    //   <Grid item style={{ marginRight: "-5rem", marginTop: "0rem" }}>
    //     <Box mt={5}>
    //       <TextTypography variant="h4" align="center" gutterBottom>
    //         {title}
    //       </TextTypography>
    //     </Box>
    //     </Grid>
    //   </Grid>
//       <Grid container direction="row" justify="space-between">
//         <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
//           <SpecialButton title={prevPageTitle} onClick={() => goToPage(prevPageID)}></SpecialButton>
//         </Grid>
//         {/* <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
//         </Grid> */}
//       </Grid>

//       <Grid container spacing={2}>
//         <Grid item lg={12}>
//           <Box m="2rem">
//           </Box>
//             <QA header={bodyText} questions={prompts} handleResponse={handleResponse}
//               nextPage={() => goToPage(nextPageID)} pages={pages} nextPageName={nextPageID}
//               prevResponses={promptResponses}/>
//         </Grid>
//       </Grid>
//     </div>
//   );
// }

// export default Reflection;
