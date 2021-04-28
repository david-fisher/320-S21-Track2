import Tooltip from '@material-ui/core/Tooltip';
import React from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import {Button, Typography} from '@material-ui/core';

const useStylesBootstrap = makeStyles((theme) => ({
    arrow: {
      color: "#e0e0e0", 
    },
    tooltip: {
      backgroundColor: "#e0e0e0",
      color: "#212121",
    },
  }));
  
  export default function BootstrapTooltip(props) {
    const classes = useStylesBootstrap();
  
    return (

      <Tooltip arrow placement="top-end" classes={classes} {...props}>
          <Button
            variant="contained"
            disableElevation
          >
            Back
          </Button>
      </Tooltip>
    )
  }
