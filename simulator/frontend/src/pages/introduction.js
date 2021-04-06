import React,{useEffect} from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  Button,
  makeStyles,
} from "@material-ui/core";
import { BASE_URL, STUDENT_ID } from "../constants/config";
import axios from 'axios';
import { ScenariosContext } from "../Nav";
import { GatheredInfoContext } from './simulationWindow';

import SpecialButton from './components/SpecialButton';
import MMedia from './components/MultiMedia'
import video from './video1.mp4'
import image from './umass.jpeg'
import audio from './z.mp3'
import { Link } from 'react-router-dom';

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

  console.log(props);

  const [showVid, setShowVid] = React.useState(false);
  const [introText, setIntroText] = React.useState('');
  //const [media, setMedia] = React.useState('')
  const [scenarios, setScenarios] = React.useContext(ScenariosContext);
  const classes = useStyles();

  // useEffect(() => {
  //   // backend call
  //   axios({
  //     method: 'get',
  //     url: BASE_URL + '/scenarios/intro',
  //     headers: {
  //       scenarioID: scenarios.currentScenarioID,
  //       studentID: STUDENT_ID,
  //     }
  //   }).then(response => {
  //     setIntroText(text => response.data[0].body_text);
  //     //setMedia(url => response.data[0].media_url)
  //   }).catch((err)=>{
  //     console.log("err",err);
  //     //alert(err);
  //   });
  // }, [scenarios])

  return (
    <div>
      <Box mt={5}>
        <Grid container direction="row" justify="center" alignItems="center">
          <TextTypography variant="h4" align="center" gutterBottom>
            {props.title}
          </TextTypography>
        </Grid>
      </Box>
      {/* <Grid container direction="row" justify="space-between">
        {/* <Grid
          item
          style={{
            marginLeft: "0rem",
            marginRight: "0rem",
            marginTop: "-3rem",
          }}
        >
          <SpecialButton 
            type={"back"}
            onClick={() => props.changePage(-1)}
          />
        </Grid>
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <SpecialButton 
            type={"next"}
            onClick={() => props.changePage(1)}
          />
        </Grid> */}
      {/* </Grid> */}
      <Grid container spacing={2}>
        <Grid item lg={12}>
          <Box p={2} className={classes.textBox}>
            {props.content}
          </Box>
          {/* could change the parameter to just scenario in the future to be more dynamic */}
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
