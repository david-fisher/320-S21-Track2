import React, { useContext, useEffect } from "react";
import { makeStyles, withStyles, Typography, Box, Grid, Button,
  Card, CardContent, Modal, Dialog, DialogContent, DialogContentText } from "@material-ui/core";
import { useTheme } from "@material-ui/core/styles";
import { GatheredInfoContext } from './simulator_window';
import { BASE_URL, STUDENT_ID, SCENARIO_ID } from "../constants/config";
import axios from 'axios';
import Conversation from './conversation';
import { ScenariosContext } from "../Nav";
import NextButton from "./components/Buttons/NextButton";
import BackButton from "./components/Buttons/BackButton";
import { ConvLimitConsumer } from './context/ConvContext';

const TextTypography = withStyles({
  root: {
    color: "#373a3c"
  }
})(Typography);

const introText = "Please select the Stakeholder you would like to interact with...";



function ellipses(str, cutoff) {
  let newStr = str;
  if (str.length >= cutoff) {
    newStr = str.substring(0, cutoff - 1) + '…';
    let lastSpace = newStr.lastIndexOf(' ');
    if (lastSpace !== -1) {
      newStr = newStr.substring(0, lastSpace) + '…';
    }
  }
  return newStr;
}

function Stakeholders(props) {
  const theme = useTheme();
  const [stakeholders, setStakeholders] = React.useState([])
  const [scenarios, setScenarios] = React.useContext(ScenariosContext);
  const [conversationLimit, setConversationLimit] = React.useState(0);
  const [stakeholdersDisabled, setStakeholdersDisabled] = React.useState({});
  const cardStyles = makeStyles({
    root: {
      width: 275,
      height: 156,
      wordBreak: 'break-word'
    },
    name: {
      color: theme.palette.primary.main
    },
    background: {
      color: '#444e58'
    },
    disabled: {
      backgroundColor: '#f9f9f9',
      color: '#c2c2c2'
    }
  });
  const [modalOpenToggles, setModalOpenToggles] = React.useState({});
  const [gatheredInfo, setGatheredInfo] = useContext(GatheredInfoContext);
  const [showStakeholders, setShowStakeholders] = React.useState(true);
  const [numStakeholderTalkedTo, setNumStakeholderTalkedTo] = React.useState(0)
  const [currentStakeholder, setCurrentStakeholder] = React.useState({});
  const [stakeholders_had, setStakeholders_had] = React.useState([]);
  const createdCardStyles = cardStyles();
  const stakeholdersGrid = getStakeholdersGrid(stakeholders);
  const [limit, setLimit] = React.useState(0);


  /** 
   * TODO: When the backend team makes this endpoint, configure it.
  */
  // React.useEffect(() => {
  //   (async () => {
  //     await axios({
  //       method: 'get',
  //       url: BASE_URL + '/scenarios/stakeholders',
  //       headers: {
  //         scenarioID: scenarios.currentScenarioID,
  //         studentID: STUDENT_ID
  //       }
  //     }).then(response => {
  //       setConversationLimit(response.data.conversation_limit)
  //       const holders = response.data.stakeholders;
  //       setStakeholders(holders);
  //       setStakeholdersDisabled(prev => {
  //         return holders.reduce((obj, stakeholder) => {
  //           obj[stakeholder.id] = false;
  //           return obj;
  //         }, {});
  //       });
  //       setModalOpenToggles(prev => {
  //         return holders.reduce((obj, stakeholder) => {
  //           obj[stakeholder.id] = false;
  //           return obj;
  //         }, {});
  //       });

  //       axios({
  //         method: 'get',
  //         url: BASE_URL + '/scenarios/stakeholders/history',
  //         headers: {
  //           scenarioID: scenarios.currentScenarioID,
  //           studentID: STUDENT_ID
  //         }
  //       }).then(histResponse => {
  //         const history = histResponse.data;
  //         setNumStakeholderTalkedTo(history.length);
  //         if (history.length >= response.data.conversation_limit) {
  //           setStakeholdersDisabled(prev => {
  //             return holders.reduce((obj, stakeholder) => {
  //               obj[stakeholder.id] = true;
  //               return obj
  //             }, {});
  //           });
  //         } else {
  //           setStakeholdersDisabled(prev => {
  //             let newDisabled = {...prev};
  //             holders.forEach(stakeholder => {
  //               let containsID = false;
  //               for (let i = 0; i < history.length; ++i){
  //                 if (stakeholder.id === history[i].stakeholder_id){
  //                   containsID = true;
  //                 }
  //               }
  //               if (containsID) {
  //                 newDisabled[stakeholder.id] = true;
  //               }
  //             });
  //             return newDisabled;
  //           });
  //         }
  //       }).catch(err => {
  //         console.log(err);
  //       });
  //     }).catch(err => {
  //       console.log(err);
  //       //alert(err);
  //     });
  // })()
  // }, [scenarios])

  /**
   * Gets stakeholders to show for the page.
   * NOTE: Every stakeholder is returned with current endpoint. The hook filters out the correct
   * ones for the current scenario. NEEDS TO BE CHANGED when endpoint works.
   */
  useEffect(() => {
    fetch(`${BASE_URL}/get_stakeholders/?scenario_id=${props.match.params.sid}`)
    .then(response => response.json())
    .then(data => {

      let results = data.slice();

      setStakeholders(results);

    })
  }, [scenarios]);
 
  useEffect(() => {
    fetch(`${BASE_URL}/get_scenario/?scenario_id=${props.match.params.sid}`)
    .then(response => response.json())
    .then(data => {
      let newLimit = data.num_conversation
      setLimit(newLimit)
    })
  }, []);

  useEffect(() => {
    fetch(`${BASE_URL}/stakeholders_had/?scenario_id=${props.match.params.sid}&student_id=${STUDENT_ID}`)
    .then(response => response.json())
    .then(data => {
      console.log("limit: " + limit)
      console.log("nstt: " + numStakeholderTalkedTo)
      console.log(stakeholders)
      setNumStakeholderTalkedTo(data.length)
      let newDisabled = {}
      if (numStakeholderTalkedTo < limit) {
        data.forEach(ele => {
          newDisabled[ele] = true
        });
      }
      else {
        stakeholders.forEach(ele => {
          newDisabled[ele.id] = true
        });
      }
      setStakeholdersDisabled(newDisabled)
    })
    .catch(err => {
      console.log(err)
    })
  }, [limit, stakeholders])


  function getStakeholderCards(id, name, isMultipart, designation, description, styles) {
    const PAGE_ID_OF_PAGE_BEFORE_CONVERSATIONS = 'gatheredInformation';

    function toggleModal(id, toggle) {
      setModalOpenToggles(prev => {
        let newToggles = {...prev};
        newToggles[id] = toggle;
        return newToggles;
      });
    }
    let cardClass, nameClass, descriptionClass;
    if (stakeholdersDisabled[id]) {
      cardClass = `${styles.root} ${styles.disabled}`;
      nameClass = descriptionClass = styles.disabled;
    } else {
      cardClass = styles.root;
      nameClass = styles.name;
      descriptionClass = styles.background;
    }
    return (
      <>
        <Button disabled={stakeholdersDisabled[id]} style={{textTransform: 'none'}} onClick={() => toggleModal(id, true)}>
          <Card className={cardClass}>
            <CardContent>
              <Typography variant="h5" component="h2" align='left' className={nameClass}>
                {name}
              </Typography>
              <Typography variant="body1" component="p" align='left'>
                {designation}
              </Typography>
              <Typography variant="body2" component="p" align='left' className={descriptionClass}>
                {ellipses(description, 87)}
              </Typography>
            </CardContent>
          </Card>
        </Button>
        <Dialog
          open={modalOpenToggles[id]}
          onClose={() => toggleModal(id, false)}
          maxWidth = {'md'}
          >
          <DialogContent>
            <DialogContentText color = "#000000">{description}</DialogContentText>
              <ConvLimitConsumer>
              {(context) => (
                  <Button variant="contained" onClick={() => {
                      setCurrentStakeholder(prev => ({
                        name: name,
                        id: id,
                        isMultipart: isMultipart
                      }));
                      setStakeholdersDisabled(prev => {
                        let newStakeholdersDisabled = {};
                        if (numStakeholderTalkedTo + 1 >= limit) {
                          for (let i=0; i<stakeholders.length; ++i) {
                            newStakeholdersDisabled[stakeholders[i].id] = true;
                          }
                        }else {
                          newStakeholdersDisabled = {...prev};
                          newStakeholdersDisabled[id] = true;
                        }
                        return newStakeholdersDisabled;
                      });
                      setNumStakeholderTalkedTo(prev => {
                        return (prev + 1)
                      });
                      // axios({
                      //   method: 'put',
                      //   url: BASE_URL + '/scenarios/stakeholders',
                      //   data: {
                      //     scenarioID: scenarios.currentScenarioID,
                      //     studentID: STUDENT_ID,
                      //     stakeholderID: id
                      //   }
                      // }).catch(err => {
                      //   console.error(err);
                      //   alert(err);
                      // })
                      setShowStakeholders(false);
                      toggleModal(id, false);
                      // setGatheredInfo(infos => {
                      //   let ind = infos.findIndex(info => info.pageId === PAGE_ID_OF_PAGE_BEFORE_CONVERSATIONS);
                      //   if (ind < 0) { ind = infos.length; }
                      //   let newInfos = [...infos];
                      //   newInfos.splice(ind, 0,
                      //     { name: name, id: `stakeholder:${id}`, pageId: 'stakeholders'});
                      //   return newInfos;
                      // });
                }}>Continue
              </Button> )}
            </ConvLimitConsumer>
          </DialogContent>
        </Dialog>
      </>
    )
  }

  function getStakeholdersGrid(stakeholders) {
    let items = stakeholders.map(stakeholder => getStakeholderCards(
      stakeholder.id, stakeholder.name, stakeholder.enable_multi_convo, stakeholder.designation, stakeholder.description, createdCardStyles));
    return (
      <div>
        <Grid container spacing={3} justify={'center'}>
          {items.map(item => ((
            <Grid item>
              {item}
            </Grid>
          )))}
        </Grid>
      </div>
    )
  }

  return (
    <div id="stakeholders">
      {showStakeholders &&
        <div id="stakeholder_cards">
          <Box mt={5}>
            <TextTypography variant="h4" align="center" gutterBottom>
              {props.title}
            </TextTypography>
          </Box>
          <Grid container spacing={2}>
          <Grid item lg={12} md={12} sm={12}>
            <Box m="1rem" align={'center'}>
              <ConvLimitConsumer>
                {(context) => (
                  <TextTypography>
                    You've spoken to <b>{numStakeholderTalkedTo} out of {limit}</b> stakeholders
                  </TextTypography>
                )}
              </ConvLimitConsumer>
            </Box>
            <TextTypography variant="body1" align="center">
              {props.content}
            </TextTypography>
          </Grid>
            {stakeholdersGrid}
          </Grid>
        </div>
      }
      {!showStakeholders &&
        <Conversation page_id={props.id} match={props.match} stakeholder={currentStakeholder} showStakeholders={showStakeholders} setShowStakeholders={setShowStakeholders} />
      }
    </div>
  );
}

export default Stakeholders;
