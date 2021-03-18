import React,{useEffect} from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  Button,
  makeStyles,
} from "@material-ui/core";
import { BASE_URL, STUDENT_ID, SCENARIO_ID } from "../constants/config";
import axios from 'axios';
import HTMLRenderer from './components/htmlRenderer';
import { ScenariosContext } from "../Nav";
import { GatheredInfoContext } from './simulationWindow';
import MMedia from './components/MultiMedia'
import video from './video1.mp4'
import image from './umass.jpeg'
import audio from './z.mp3'

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

function Introduction({ pages, setPages, activePage, setActivePage }) {
  
  const [gatheredInfo, setGatheredInfo] = React.useContext(GatheredInfoContext);

  function goToProjectAssignment() {
    if (!pages.projectAssignment.visited) {
      setPages((prevPages) => {
        let copy = { ...prevPages };
        copy.projectAssignment.visited = true;
        return copy;
      });
      setGatheredInfo(infos => {
        let newInfos = [...infos];
        newInfos.push({id: 'page', name: 'Project Assignment', pageId: 'projectAssignment'});
        return newInfos;
      });
    }
    setActivePage((prevPage) => "projectAssignment");

  }

  const [showVid, setShowVid] = React.useState(false);
  const [introText, setIntroText] = React.useState('');
  const [media, setMedia] = React.useState('')
  const [scenarios, setScenarios] = React.useContext(ScenariosContext);
  const classes = useStyles();

  useEffect(() => {
    // backend call
    axios({
      method: 'get',
      url: BASE_URL + '/scenarios/intro',
      headers: {
        scenarioID: scenarios.currentScenarioID,
        studentID: STUDENT_ID,
      }
    }).then(response => {
      setIntroText(text => response.data[0].body_text);
      setMedia(url => response.data[0].media_url)
    }).catch((err)=>{
      console.log("err",err);
      //alert(err);
    });
  }, [scenarios])

  return (
    <div>
      <Box mt={5}>
        <Grid container direction="row" justify="center" alignItems="center">
          <TextTypography variant="h4" align="center" gutterBottom>
            Introduction
          </TextTypography>
        </Grid>
      </Box>
      <Grid container direction="row" justify="space-between">
        <Grid
          item
          style={{
            marginLeft: "0rem",
            marginRight: "0rem",
            marginTop: "-3rem",
          }}
        >
          {/*  <Button>Back</Button>*/}
        </Grid>
        <Grid item style={{ marginRight: "0rem", marginTop: "-3rem" }}>
          <Button
            variant="contained"
            disableElevation
            color="primary"
            onClick={goToProjectAssignment}
          >
            Next
          </Button>
        </Grid>
      </Grid>
      <Grid container spacing={2}>
        <Grid item lg={12}>
          <Box p={2} className={classes.textBox}>
            <HTMLRenderer html={introText}/>
          </Box>
          {/* could change the parameter to just scenario in the future to be more dynamic */}
          <MMedia source={media} name="Brain Pop Ethics" description="Example video from link." height={300} type='link' /> 
          <MMedia source={video} name="Cool Sky Video" description="Example local MP4 type video." height={300} type='video' />
          <MMedia source={image} name="UMass picture" description="Example image of our beautiful campus." height={300} type='image' />
          <MMedia source={audio} name="Random music" description="Example MP3 file randomly found online." height={200} type='audio' />
        </Grid>
      </Grid>
    </div>
  );
}

export default Introduction;
