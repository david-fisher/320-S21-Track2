import React from "react";
import {
  makeStyles,
  Typography,
  Paper,
  Stepper,
  Step,
  StepLabel,
  StepContent,
  Button,
  Box,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  button: {
    marginTop: theme.spacing(1),
    marginRight: theme.spacing(1),
  },
  actionsContainer: {
    marginBottom: theme.spacing(2),
  },
  resetContainer: {
    padding: theme.spacing(3),
  },
  step: {
    "&$completed": {
      color: "#881C1C",
    },
    "&$active": {
      color: "#881C1C",
    },
    "&$disabled": {
      color: "#444e58",
    },
  },
  active: {},
  completed: {},
  disabled: {},
}));


// gets steps to be shown in stepper...returns array of buttons
function getSteps(pages, navigatePageFunc) {
  let stepArr = [];
  let keys = Object.keys(pages);
  let values = Object.values(pages);

  values.forEach((page) => {
    let buttonName = page.props.title;
    if(page.visited === false)
      stepArr.push(<Button disabled>{buttonName}</Button>);
    else
      stepArr.push(
      <Button
        style={{color: "#881c1c"}}
        onClick={() => navigatePageFunc(page)}  
      >
        {buttonName}
      </Button>)
  })
  return stepArr;
}

function getStepContent(step) {
  switch (step) {
    case 0:
      return "";
    case 1:
      return "";
    case 2:
      return "";
    default:
      return "";
  }
}

export default function VerticalLinearStepper(props) {
  //<Stepper activePage={activePage} pages={pages} />
  const classes = useStyles();
  // eslint-disable-next-line
  const [activeStep, setActiveStep] = React.useState(props.activePage);
  
  function navigatePage(page) {
    if(page.props.completed){
      if (!page.props.visited) {
        props.setPages(prevPages => {
          console.log("Prevpages" + prevPages)
          let copy = {...prevPages};
          copy[page].visited = true;
          return copy;
        });
      }
      console.log("Props" + props);
      props.setActivePage(page)
    }   
  }

  const steps = getSteps(props.pages, navigatePage);
  steps.map((label, index) => (console.log("here " + index, label)));
  return (
    <div className={classes.root}>
      <Box mt={3} ml={1}>
        <Stepper activeStep={activeStep} orientation="vertical">
          {steps.map((label, index) => (
            <Step
              key={index}
              classes={{
                root: classes.step,
                completed: classes.completed,
                active: classes.active,
              }}
            >
              <StepLabel
                StepIconProps={{
                  classes: {
                    root: classes.step,
                    completed: classes.completed,
                    active: classes.active,
                  },
                }}
              >
                {label}
              </StepLabel>
              <StepContent>
                <Typography>{getStepContent(index)}</Typography>
                <div className={classes.actionsContainer}>
                  <div></div>
                </div>
              </StepContent>
            </Step>
          ))}
        </Stepper>
        {activeStep === steps.length && (
          <Paper square elevation={0} className={classes.resetContainer}>
            <Typography>All steps completed - you&apos;re finished</Typography>
          </Paper>
        )}
      </Box>
    </div>
  );
}
