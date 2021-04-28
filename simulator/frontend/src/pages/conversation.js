import React, { useEffect } from "react";
import {
  withStyles,
  Typography,
  Box,
  Grid,
  Button,
  makeStyles,
} from "@material-ui/core";
import { BASE_URL } from "../constants/config";
import { ScenariosContext } from "../Nav";
import MultipartConvo from './multipart_conversation';

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

function Conversation({ showStakeholders, setShowStakeholders, stakeholder }) {
  console.log(stakeholder);
  function goToStakeholders() {
    setShowStakeholders(true);
  }

  const [monologue, setMonologue] = React.useState('');
  const [ dialogue, setDialogue ] = React.useState({});
  const [scenarios, setScenarios] = React.useContext(ScenariosContext);

  const getConversationData = async () => {

    const response = await fetch(`${BASE_URL}/stakeholder_conv/?stakeholder_id=${stakeholder.id}`);

    if(!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  };

  const setConversation = (conversation) => {

    console.log(conversation);

    if(!stakeholder.isMultipart) {
      setMonologue(conversation.reduce((text, convPart) => {
        return text + convPart.response;
      }, ''));
    } else {
      setDialogue(conversation.map((convo) => {
        return {
          question: convo.question,
          response: convo.response
        }; 
      }));
    }

  };

  useEffect(() => {
    getConversationData().then(conversationData => {
      console.log(conversationData);
      setConversation(conversationData);
      //setMonologue(conversationData[0].response);
    })
    .catch(err => {
      alert(err);
    })
  }, [scenarios])

  const classes = useStyles();

  return (
    <div>
      <Box mt={5}>
        <Grid container direction="row" justify="center" alignItems="center">
          <TextTypography variant="h4" align="center" gutterBottom>
            {stakeholder.name}
          </TextTypography>
        </Grid>
      </Box>
      <Grid item style={{ marginLeft: "0rem", marginTop: "-3rem" }}>
        <Button
          variant="contained"
          disableElevation
          color="primary"
          onClick={goToStakeholders}
        >
          Return
            </Button>
      </Grid>
      <Grid container direction="row" justify="space-between">
        <Grid
          item
          style={{
            marginLeft: "0rem",
            marginRight: "0rem",
            marginTop: "-3rem",
          }}
        >
        </Grid>
      </Grid>
      <Grid container spacing={2}>
        <Grid item lg={12}>
          <Box p={2} className={classes.textBox}>
            <Typography>
              {stakeholder.isMultipart ? <MultipartConvo dialogue={dialogue} /> : monologue}
            </Typography>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
}

export default Conversation;