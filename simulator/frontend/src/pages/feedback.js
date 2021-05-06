import React from "react";
import { withStyles,Typography, Box, Grid } from "@material-ui/core";
import Radar from "./chart/chart";

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
          <SpecialButton type="back" title="Summary" onClick={goToSummary}></SpecialButton>
        </Grid>
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <SpecialButton type="next" title="Final Reflection" onClick={goToFinalReflection}></SpecialButton>
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