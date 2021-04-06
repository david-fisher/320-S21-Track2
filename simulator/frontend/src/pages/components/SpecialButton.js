import Tooltip from '@material-ui/core/Tooltip';
import React from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import {Button, Typography} from '@material-ui/core';

const useStylesBootstrapBack = makeStyles((theme) => ({
    arrow: {
      color: "#e0e0e0", 
    },
    tooltip: {
      backgroundColor: "#e0e0e0",
      color: "#212121",
    },
  }));
  const useStylesBootstrapNextSubmit = makeStyles((theme) => ({
    arrow: {
      color: "#881c1c", 
    },
    tooltip: {
      backgroundColor: "#881c1c",
    },
  }));
  
  export default function BootstrapTooltip(props) {
    const nextSubmitClasses = useStylesBootstrapNextSubmit();
    const backClasses = useStylesBootstrapBack();
    const { type, ...other} = props;
    let useClasses = nextSubmitClasses;
    let tooltipPosition = "top-end";
    let buttonVariant = "contained";
    let buttonColor = "primary";

    if (props.type === "back"){
      useClasses = backClasses; 
      buttonColor = "#e0e0e0";
    }
    else if (props.type === "submit"){
      tooltipPosition = "bottom";
      buttonVariant = "outlined";
    }
    return (
      <Tooltip arrow placement={tooltipPosition} classes={useClasses} {...props}>
          <Button
            variant={buttonVariant}
            disableElevation
            color={buttonColor}
          >
            {type}
          </Button>
      </Tooltip>
      
    )
  }