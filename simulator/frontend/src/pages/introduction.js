import React from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  makeStyles,
} from "@material-ui/core";
import { ScenariosContext } from "../Nav";
import MMedia from './components/MultiMedia';
import video from './video1.mp4';
import image from './umass.jpeg';
import audio from './z.mp3';

const TextTypography = withStyles({
  root: {
    color: "#373a3c",
    whiteSpace: "pre-line", 
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

function Introduction(props) {

  const [scenarios, setScenarios] = React.useContext(ScenariosContext);
  const classes = useStyles();

  return (
    <div>
      <Box mt={5}>
        <Grid container direction="row" justify="center" alignItems="center">
          <TextTypography variant="h4" align="center" gutterBottom>
            {props.title}
          </TextTypography>
        </Grid>
      </Box>
      <Grid container spacing={2}>
        <Grid item lg={12}>
          <Box p={2} className={classes.textBox}>
            {props.content}
          </Box>
          {/* <MMedia source={media} name="Brain Pop Ethics" description="Example video from link." type='link' />  */}
          <MMedia source={video} name="Cool Sky Video" description="Example local MP4 type video." type='video' />
          <MMedia source={image} name="UMass picture" description="Example image of our beautiful campus." type='image' />
          <MMedia source={audio} name="Random music" description="Example MP3 file randomly found online." type='audio' />
        </Grid>
      </Grid>
    </div>
  );
}

export default Introduction;
