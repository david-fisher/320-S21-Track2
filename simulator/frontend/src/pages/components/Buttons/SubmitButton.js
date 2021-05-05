import Tooltip from '@material-ui/core/Tooltip';
import React from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import {Button} from '@material-ui/core';

const useStylesBootstrap = makeStyles((theme) => ({
    arrow: {
      color: "#881c1c", 
    },
    tooltip: {
      backgroundColor: "#881c1c",
    },
  }));
  
  export default function BootstrapTooltip(props) {
    const classes = useStylesBootstrap();
  
    return (

      <Tooltip arrow placement="bottom" classes={classes} {...props}>
          <Button type="submit" variant="outlined" color="primary" className={classes.button}>
            Submit
          </Button>
      </Tooltip>
    )
  }
