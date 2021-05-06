import React, { useEffect, useState, useRef } from "react";
import { withStyles,Typography, Box, Grid, Button} from "@material-ui/core";
import Radar from "./chart/chart"
import ScrollableTabsButtonAuto from "./components/feedback_tabs";
import NextButton from "./components/Buttons/NextButton"
import BackButton from "./components/Buttons/BackButton"
import { BASE_URL, STUDENT_ID } from '../constants/config';
//import { useFetch } from "react-async"

const TextTypography = withStyles({
  root: {
    color: "#373a3c"
  }
})(Typography);

// visited, completed, pageNumber, type, nextPageNumber, title, content, match, activePage, changePage
function Feedback(props) {
  // function goToSummary(){
  //   if (!pages.summary.visited) {
  //     setPages(prevPages => {
  //       let copy = {...prevPages};
  //       copy.summary.visited = true;
  //       return copy;
  //     });
  //   }
  //   setActivePage(prevPage => 'summary')
  // }

  // function goToFinalReflection(){
  //   if (!pages.finalReflection.visited) {
  //     setPages(prevPages => {
  //       let copy = {...prevPages};
  //       copy.finalReflection.visited = true;
  //       return copy;
  //     });
  //   }
  //   setActivePage(prevPage => 'finalReflection')
  // }

  return (
    <div>
      <Grid container direction="row" justify="center" alignItems="center">
        <Box mt = {5}>
          <TextTypography variant="h4" align="center" gutterBottom>
            {props.title}
          </TextTypography>
        </Box>
      </Grid>
      {/* <Grid container direction="row" justify="space-between">
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <BackButton title="Summary" onClick={goToSummary}></BackButton>
        </Grid>
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <NextButton title="Final Reflection" onClick={goToFinalReflection}></NextButton>
        </Grid>
      </Grid> */}
      <Grid container spacing={2}>
        <Grid lg={12}>
          <Box m="2rem">
          <Radar match={props.match} /> 
          </Box>
          <TextTypography variant="body1">
            {props.content}
          </TextTypography>
        </Grid>
      </Grid>
      <Grid container spacing={2}>
        <Grid lg={12}>
          {/* <ScrollableTabsButtonAuto/> */}
        </Grid>
      </Grid>
    </div>
  );
}

export default Feedback;