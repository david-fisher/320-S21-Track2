import React, { useEffect } from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  makeStyles,
} from "@material-ui/core";
import { BASE_URL, STUDENT_ID, SCENARIO_ID }from "../constants/config";
import SpecialButton from './components/SpecialButton';
import TextField from '@material-ui/core/TextField';
import axios from "axios";
import SpecialButton from './components/SpecialButton';


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
  const [userInput, setUserInput] = React.useState({});
  const [data, setData] = React.useState([]);
  const [isresponse,setIsresponse] = React.useState(false);
  const [reflectionQuestion,setrefelctionQuestion] = React.useState([]);
  function  handleResponse(userResponse){
    for(const[key,value] of Object.entries(userResponse)){
      const items = {
        response: key,
        student: String(STUDENT_ID),
        scenario: SCENARIO_ID,
        version:2,
        page:props.id,
        course: 1,
        choice:'none',
        reflection:value
      };
      axios.post(BASE_URL + `/reflection_response/?page_id=${props.id}&student_id=${STUDENT_ID}&scenario_id=${SCENARIO_ID} `,items)
      .then(response=>{console.log(response.data.reflections)
        setIsresponse(true)})
      .catch(e=>{console.log(e)})
   }
  }
   const handleChange = (event) => {
    //  console.log("This is handle change")
     let response_id = event.target.id
     setUserInput({...userInput,[response_id]:document.getElementById(event.target.id).value})
    // setUserInput(event.target.value);
  };
  // console.log(userInput)
  // console.log("Test end here")
  const classes = useStyles();
  
  useEffect(()=>{
    fetch(BASE_URL + `/reflection_response/?page_id=${props.id}&student_id=${STUDENT_ID}&scenario_id=${SCENARIO_ID} `)
    .then(response=>response.json())
    .then(temp=> {
       console.log("This is temp")
       console.log(temp)
       if(temp.detail){
        setData([])
       }else{
      const mapped = temp.map(({reflections,response}) =>{
          return [reflections,response]
        })
      setData(mapped);
      }
    })
    fetch(BASE_URL + `/get_page_info/?page_id=${props.id}`).then(response=>response.json())
    .then(({ body })=>{
      setrefelctionQuestion([...reflectionQuestion, ...body])
    })
  },[])
  const isDisable = (items,reflection_question_id)=>{
    var arr = items.filter( x=>{
      if(typeof x ==='undefined'){
        return false
      }
      if(x[1]===reflection_question_id){
        return true
      }
    })
    return arr.length
  }
  const isempty = (items,reflection_question_id)=>{
    var value =  items.find( x=>{
      if(typeof x ==='undefined'){
        return ""
      }
      if(x[1]===reflection_question_id){
        console.log(x[0])
        return x[0]
      }
    })
    if(typeof value === 'undefined'){
      return ""
    }
    return value[0]
  }
  const frams = reflectionQuestion.map(({reflection_question,reflection_question_id}) =>
    <Grid container spacing={2}>
         <Grid item lg={12}>
           <Box m="2rem">
           </Box>
           <Box p={2} className={classes.textBox}>
           <TextTypography variant="body1" paragraph = {true} gutterBottom>
             {reflection_question}
          </TextTypography>
          </Box>
         <Box pt={2}>
         <Typography variant="body1" paragraph = {true} gutterBottom>
              <TextField
                required
                disabled = {isDisable(data,reflection_question_id)}
                fullWidth = {true}
                defaultValue = {isempty(data,reflection_question_id)}
                multiline = {true}
                autoComplete = "off"
                id={reflection_question_id}
                label="Required"
                variant="filled"
                onChange =  {handleChange}
                InputLabelProps = {{shrink:true}}
              />
          </Typography>
         </Box>
         </Grid>
    </Grid>
  );
  // console.log(reflectionQuestion);
  return(
    <div>
    <Box mt={5}>
      <Grid container direction="row" justify="center" alignItems="center">
        <TextTypography variant="h4" align="center" gutterBottom>
          {props.title}
        </TextTypography>
      </Grid>
        {frams}
        {/* <Grid container spacing={2}>
         <Grid item lg={12}>
           <Box m="2rem">
           </Box>
           <Box p={2} className={classes.textBox}>
           <TextTypography variant="body1" paragraph = {true} gutterBottom>
             {props.content}
          </TextTypography>
          </Box>
         </Grid>
       </Grid> */}
       {/* <Grid container spacing={2}>
         <Grid item lg={12}>
           <Box m="2rem">
           </Box>
           <Typography variant="body1" paragraph = {true} gutterBottom>
              <TextField
                required
                disabled = {isresponse}
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
       </Grid> */}
       <Box pt={2}>
          <SpecialButton title="submit" onClick={() => handleResponse(userInput)}/>
        </Box>
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
