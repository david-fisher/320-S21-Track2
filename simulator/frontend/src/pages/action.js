import React,{useEffect} from "react";
import { makeStyles, withStyles, Typography, Box, Button, Grid } from "@material-ui/core";
import Checkbox from "./components/checkbox";
import { BASE_URL, STUDENT_ID, SCENARIO_ID } from "../constants/config";
import axios from 'axios';
import { ScenariosContext } from "../Nav";
import HTMLRenderer from "./components/htmlRenderer";
import BackButton from "./components/Buttons/BackButton"
import SubmitButton from "./components/Buttons/SubmitButton"

// const useStyles = makeStyles((theme) => ({
//   root: {
//     backgroundColor: theme.palette.background.paper,
//     color: "#5b7f95"
//   },
// }));

const TextTypography = withStyles({
  root: {
    color: "#373a3c"
  }
})(Typography);

// visited, completed, pageNumber, type, nextPageNumber, title, content, match, activePage, changePage
//function Action({ pages, setPages, activePage, setActivePage, content_url, nextPageID, prevPageID, title }) {
function Action(props) {
  // function goToPage(pageID) {
  //   if (pages[pageID].completed) {
  //     if (!pages[pageID].visited) {
  //       setPages((prevPages) => {
  //         let copy = { ...prevPages };
  //         copy[pageID].visited = true;
  //         return copy;
  //       });
  //     }
  //     setActivePage((prevPage) => pageID);
  //   }
  // }

  // let prevPageTitle = "";
  // const [actionQuestion, setActionQuestion] = React.useState('');
  // const [questionID, setQuestionID] = React.useState('');
  // const [scenarios, setScenarios] = React.useContext(ScenariosContext);

  // const [actionChoices, setActionChoices] = React.useState([]);

  // useEffect (() => {
  //   fetch(BASE_URL + '/action_page/')
  //   .then(res => res.json())
  //   .then(actionData => {
  //     let choices = []
  //     actionData.results.forEach(element => {
  //       let choice = {
  //         text: element.choice,
  //         result_page: element.result_page
  //       }
  //       choices.push(choice)
  //     });
  //     setActionChoices(choices)
  //   })
  // }, [])

  // useEffect(() => {
  //   // backend call
  //   (async () => {
  //     axios({
  //       method: 'get',
  //       url: BASE_URL + content_url,
  //       headers: {
  //         scenarioID: scenarios.currentScenarioID,
  //         studentID: STUDENT_ID,
  //       }
  //     }).then(response => {
  //       console.log(response);
  //       if (scenarios.currentScenarioID == 1)
  //       {
  //         setActionQuestion(text => response.data[0].question);
  //         setQuestionID(id => response.data[0].option_id);
  //       }
  //       if (scenarios.currentScenarioID == 2){
  //         setActionQuestion(text => response.data[1].question);
  //         setQuestionID(id => response.data[1].option_id);
  //       }
  //     }).catch((err)=>{
  //       console.log("err",err);
  //       //alert(err);
  //     });
  //   })();
  // }, [scenarios]);


  // async function handleResponse(data) {
  //   const request_data = {}
  //   console.log("Question ID's " + questionID);
  //   request_data[questionID[0].toString()] = data;
  //   await axios({
  //     url: BASE_URL,
  //     method: 'put',
  //     data: {
  //       scenarioID: scenarios.currentScenarioID,
  //       studentID: STUDENT_ID,
  //       data: request_data
  //     }
  //   });
  // }

  // function getPrevPageTitle(prevPageID) {
  //   switch (prevPageID) {
  //     case "initialReflection": prevPageTitle = "Initial Reflection";
  //     break;
  //     case "middleReflection": prevPageTitle = "Middle Reflection";
  //     break;
  //     default:
  //       break;
  //   }
  // }
  // getPrevPageTitle(prevPageID);
  
  return (
    <div>
      <Grid container direction="row" justify="center" alignItems="center">
        <Box mt={5}>
          <TextTypography variant="h4" align="center" gutterBottom>
            {props.title}
          </TextTypography>
        </Box>
      </Grid>
      {/*       
      <Grid container direction="row" justify="space-between">
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <BackButton title={prevPageTitle} onClick={() => goToPage(prevPageID)}>
          </BackButton>
        </Grid>
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
      addtional comment was on this line  <Button variant="contained" disableElevation color="primary" onClick={() => goToPage(nextPageID)} >Next</Button>
        </Grid>
      </Grid>
       */}
      <Grid container spacing={2}>
        <Grid item lg={12}>
          <Box m="2rem">
          </Box>
          <HTMLRenderer html={props.content}/>
        </Grid>
        <Grid item lg={12}>
        <Checkbox pageNumber={props.pageNumber} changePage={props.changePage} pageId={props.id} match={props.match}/> 
        </Grid>
      </Grid>
    </div>

  );
}

export default Action;