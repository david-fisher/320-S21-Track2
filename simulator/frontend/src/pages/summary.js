import React from "react";
import { withStyles, Typography, Box, Grid } from "@material-ui/core";
import ScrollableTabsButtonAuto from "./components/tabs"
import SpecialButton from "./components/SpecialButton"

const TextTypography = withStyles({
  root: {
    color: "#373a3c"
  }
})(Typography);

function Summary({pages, setPages, activePage, setActivePage}) {
  function goToFinalAction(){
    if (!pages.finalAction.visited) {
      setPages(prevPages => {
        let copy = {...prevPages};
        copy.finalAction.visited = true;
        return copy;
      });
    }
    setActivePage(prevPage => 'finalAction')
  }
  function goToFeedback(){
    if (!pages.feedback.visited) {
      setPages(prevPages => {
        let copy = {...prevPages};
        copy.feedback.visited = true;
        return copy;
      });
    }
    setActivePage(prevPage => 'feedback');
  }
  
  return (
    <div>
      <Grid container direction="row" justify="center" alignItems="center">
        <Box mt = {5}>
          <TextTypography variant="h4" align="center" gutterBottom>
            Summary
          </TextTypography>
        </Box>
      </Grid>
      <Grid container direction="row" justify="space-between">
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <SpecialButton type="back" title="Final Action" onClick={goToFinalAction}></SpecialButton>
        </Grid>
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <SpecialButton type="next" title="Feedback" onClick={goToFeedback}></SpecialButton>
        </Grid>
      </Grid>
      <Grid container spacing={2}>
        <Grid lg={12}>
          <ScrollableTabsButtonAuto/>
        </Grid>
      </Grid>
    </div>
  );
}

export default Summary;
