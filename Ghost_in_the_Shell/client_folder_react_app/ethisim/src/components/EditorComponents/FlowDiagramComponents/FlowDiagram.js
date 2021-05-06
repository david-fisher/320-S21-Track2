import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {
    Typography,
    Button,
    Dialog,
    DialogActions,
    DialogTitle,
    DialogContent,
    Grid,
} from '@material-ui/core';
import ReactFlow, {
    removeElements,
    isEdge,
    isNode,
    MiniMap,
    Controls,
    Background,
} from 'react-flow-renderer';
import initializeElements from './HelperFunctions/initializeElements';
import {
    actionNode,
    reflectionNode,
    genericNode,
    conversationNode,
    introNode,
} from './HelperFunctions/node';
import addEdge from './HelperFunctions/addEdge';
import get from './../../../universalHTTPRequests/get';
import put from './../../../universalHTTPRequests/put';
import LoadingSpinner from '../../LoadingSpinner';
import RefreshIcon from '@material-ui/icons/Refresh';
import ErrorIcon from '@material-ui/icons/Error';
import SuccessBanner from '../../Banners/SuccessBanner';
import ErrorBanner from '../../Banners/ErrorBanner';
import PropTypes from 'prop-types';
import HelpIcon from '@material-ui/icons/Help';
import GenericInfoButton from '../../InfoButtons/GenericInfoButton';

const useStyles = makeStyles((theme) => ({
    errorContainer: {
        marginTop: theme.spacing(2),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    container: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        height: '90vh',
    },
    margin: {
        marginBottom: '15px',
    },
    title: {
        textAlign: 'center',
    },
    copyright: {
        margin: theme.spacing(2),
    },
    buttonContainer: {
        display: 'flex',
        float: 'right',
        flexDirection: 'column',
    },
    button: {
        zIndex: 5,
        float: 'right',
    },
    iconError: {
        fontSize: '75px',
    },
    iconRefreshLarge: {
        fontSize: '75px',
    },
    iconRefreshSmall: {
        fontSize: '30px',
    },
}));

//Needs scenario id
const endpointGET = '/flowchart?scenario=';
//Needs scenario id
const endpointPUT = '/flowchart?scenario=';

FlowDiagram.propTypes = {
    scenario_ID: PropTypes.number,
};

export default function FlowDiagram({ scenario_ID }) {
    const scenarioID = scenario_ID;
    const classes = useStyles();
    const [fetchedElements, setFetchedElements] = useState({
        data: null,
        loading: true,
        error: null,
    });

    const [elementsPUT, setElementsPUT] = useState({
        data: null,
        loading: false,
        error: null,
    });

    const [elements, setElements] = useState([]);
    const [unsaved, setUnsaved] = useState(false);
    const [errorText, setErrorText] = useState('');

    //for info button
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };

    function positionElements(elements) {
        let introductionElement = elements.filter((componentData) => {
            return componentData.page_type === 'I';
        });
        let genericElements = elements.filter((componentData) => {
            return componentData.page_type === 'G';
        });
        let reflectionElements = elements.filter((componentData) => {
            return componentData.page_type === 'R';
        });
        let actionElements = elements.filter((componentData) => {
            return componentData.page_type === 'A';
        });
        let stakeholderConversationElement = elements.filter(
            (componentData) => {
                return componentData.page_type === 'S';
            }
        );

        let edges = elements.filter((componentData) => {
            return isEdge(componentData);
        });

        let initialElements = introductionElement.concat(
            genericElements,
            reflectionElements,
            actionElements,
            stakeholderConversationElement,
            edges
        );

        initialElements = initialElements.map((componentData) => {
            return initializeElements(componentData);
        });

        //Set position of elements if elements are new ({x: 0,y: 0})
        //Height of nodes are 51.2 pixels
        initialElements.reduce((acc, currentValue) => {
            if (
                currentValue.position.x === 0 &&
                currentValue.position.y === 0
            ) {
                currentValue.position.y += acc;
                return acc + 51.2;
            }
            return acc;
        }, 0);

        return initialElements;
    }

    function addEdges(elements) {
        //Add edges
        elements.forEach((currentElement) => {
            //TODO
            if (currentElement.type === 'actionNode') {
                if (!currentElement.action[0]) {
                    // eslint-disable-next-line
                    throw 'Action incomplete';
                }
                //Only 2 action options
                if (currentElement.action[0].result_page) {
                    elements = addEdge(
                        {
                            source: currentElement.id.toString() + '__a',
                            target: currentElement.action[0].result_page.toString(),
                        },
                        elements
                    );
                }
                if (currentElement.action[1].result_page) {
                    elements = addEdge(
                        {
                            source: currentElement.id.toString() + '__b',
                            target: currentElement.action[1].result_page.toString(),
                        },
                        elements
                    );
                }
            } else if (currentElement.next_page) {
                elements = addEdge(
                    {
                        source: currentElement.id.toString(),
                        target: currentElement.next_page.toString(),
                    },
                    elements
                );
            }
        });

        return elements;
    }

    let getData = () => {
        setUnsaved(false);
        function onSuccess(resp) {
            setElements(addEdges(positionElements(resp.data)));
        }
        function onError(resp) {
            if (resp === 'Action incomplete') {
                setErrorText(
                    'You have at least one Action page that is incomplete (i.e. without options). You must complete all action pages before you can access the Flow Diagram.'
                );
            } else {
                setErrorText('Unable to fetch Flow Diagram! Please try again.');
            }
        }
        get(setFetchedElements, endpointGET + scenarioID, onError, onSuccess);
    };

    useEffect(getData, []);

    const [isRemoveButtonDisabled, setIsRemoveButtonDisabled] = useState(true);
    const [currentEdgeSelected, setCurrentEdgeSelected] = useState();

    const nodeTypes = {
        actionNode: actionNode,
        reflectionNode: reflectionNode,
        genericNode: genericNode,
        introNode: introNode,
        conversationNode: conversationNode,
    };

    //Height and Width of flow diagram
    const graphStyles = { width: '100%', height: '100%', border: 'solid' };

    const onConnect = (params) => {
        setUnsaved(true);
        setElements((elements) => addEdge(params, elements));
    };

    const onRemoveEdge = (params, element) => {
        if (isEdge(element)) {
            setIsRemoveButtonDisabled(false);
            setCurrentEdgeSelected([element]);
        }
    };

    const deleteEdge = () => {
        setUnsaved(true);
        if (currentEdgeSelected != null) {
            setElements((elements) =>
                removeElements(currentEdgeSelected, elements)
            );
            setCurrentEdgeSelected(null);
            setIsRemoveButtonDisabled(true);
        }
    };

    //Update of nodes position
    const onNodeDrag = (event, element) => {
        setUnsaved(true);
        //ID's in flow diagram library are stored as strings
        const index = elements.findIndex(
            (ele) => ele.id === Number(element.id)
        );
        // important to create a copy, otherwise you'll modify state outside of setState call
        let elementsCopy = [...elements];
        elementsCopy[index] = {
            ...elementsCopy[index],
            position: element.position,
        };
        setElements(elementsCopy);
    };

    const save = () => {
        function onSuccess() {
            let resetElements = elements.reduce((array, currentElement) => {
                if (isNode(currentElement) && currentElement.position.x === 0) {
                    return array.concat({
                        ...currentElement,
                        x_coordinate: 0,
                        y_coordinate: 0,
                        position: { x: 0, y: 0 },
                    });
                }
                return array.concat(currentElement);
            }, []);
            setElements(positionElements(resetElements));
            setUnsaved(false);
            setSuccessBannerFade(true);
            setSuccessBannerMessage('Successfully Saved!');
        }

        function onError() {
            setErrorBannerFade(true);
            setErrorBannerMessage('Failed to Save!');
        }

        const updatedElements = elements.reduce((array, currentElement) => {
            if (isNode(currentElement)) {
                let nodeElement = {
                    page: currentElement.page,
                    page_type: currentElement.page_type,
                    page_title: currentElement.page_title,
                    page_body: currentElement.body,
                    scenario_id: currentElement.SCENARIO_id, //WEIRD PROP
                    version: currentElement.version,
                    next_page: null,
                    x_coordinate: Math.floor(currentElement.position.x),
                    y_coordinate:
                        Math.floor(currentElement.position.x) !== 0
                            ? Math.floor(currentElement.position.y)
                            : 0,
                };
                console.log('node');
                console.log(currentElement);

                if (currentElement.type === 'actionNode') {
                    nodeElement.action = currentElement.action.map(
                        (actionData) => {
                            return {
                                id: actionData.id,
                                page: actionData.PAGE_id, //WEIRD PROP
                                choice: actionData.choice,
                                result_page: null,
                            };
                        }
                    );

                    elements.forEach((currElement) => {
                        //First option
                        if (
                            isEdge(currElement) &&
                            currElement.source === currentElement.id + '__a'
                        ) {
                            nodeElement.action[0] = {
                                id: currentElement.action[0].id,
                                choice: currentElement.action[0].choice,
                                page: currentElement.id,
                                result_page: Number(currElement.target),
                            };
                            //Second option
                        } else if (
                            isEdge(currElement) &&
                            currElement.source === currentElement.id + '__b'
                        ) {
                            nodeElement.action[1] = {
                                id: currentElement.action[1].id,
                                choice: currentElement.action[1].choice,
                                page: currentElement.id,
                                result_page: Number(currElement.target),
                            };
                        }
                    });
                } else {
                    //Set next page ID for all other node types
                    elements.some((currElement) => {
                        //currElement.source is type string, convert to number
                        if (
                            isEdge(currElement) &&
                            Number(currElement.source) === currentElement.id
                        ) {
                            //Set NEXT_PAGE id to type number
                            nodeElement.next_page = Number(currElement.target);
                            return true;
                        }
                        return false;
                    });
                }
                return array.concat(nodeElement);
            }
            return array;
        }, []);
        console.log(updatedElements);
        put(
            setElementsPUT,
            endpointPUT + scenarioID,
            onError,
            onSuccess,
            updatedElements
        );
    };

    const [successBannerFade, setSuccessBannerFade] = useState(false);
    const [successBannerMessage, setSuccessBannerMessage] = useState('');
    const [errorBannerFade, setErrorBannerFade] = useState(false);
    const [errorBannerMessage, setErrorBannerMessage] = useState('');

    useEffect(() => {
        const timeout = setTimeout(() => {
            setSuccessBannerFade(false);
        }, 1000);

        return () => clearTimeout(timeout);
    }, [successBannerFade]);

    //RESET Pop-up Dialog
    const [openReset, setOpenReset] = useState(false);
    const [openRefresh, setOpenRefresh] = useState(false);

    const refresh = () => {
        if (unsaved) {
            setOpenRefresh(true);
        } else {
            getData();
        }
    };

    const handleCloseRefresh = (refresh) => {
        setOpenRefresh(false);
        //remove all edges and reset x and y coordinates to 0
        if (refresh) {
            getData();
        }
    };

    const handleClickOpenReset = () => {
        setOpenReset(true);
    };

    const handleCloseReset = (reset) => {
        setOpenReset(false);
        //remove all edges and reset x and y coordinates to 0
        if (reset) {
            setUnsaved(true);
            let resetElements = elements.reduce((array, currentElement) => {
                if (isNode(currentElement)) {
                    return array.concat({
                        ...currentElement,
                        next_page: null,
                        x_coordinate: 0,
                        y_coordinate: 0,
                        position: { x: 0, y: 0 },
                    });
                }
                return array;
            }, []);
            setElements(positionElements(resetElements));
        }
    };

    ConfirmationDialog.propTypes = {
        onClose: PropTypes.any,
        open: PropTypes.bool,
        title: PropTypes.string,
        content: PropTypes.string,
    };

    function ConfirmationDialog({ onClose, open, title, content }) {
        const handleCancel = () => {
            onClose();
        };

        const handleOk = () => {
            onClose(true);
        };

        return (
            <Dialog
                disableBackdropClick
                disableEscapeKeyDown
                maxWidth="xs"
                aria-labelledby="confirmation-dialog-title"
                open={open}
            >
                <DialogTitle id="confirmation-dialog-title">
                    {title}
                </DialogTitle>
                <DialogContent dividers>
                    <Typography>{content}</Typography>
                </DialogContent>
                <DialogActions>
                    <Button autoFocus onClick={handleCancel} color="primary">
                        Cancel
                    </Button>
                    <Button onClick={handleOk} color="primary">
                        Ok
                    </Button>
                </DialogActions>
            </Dialog>
        );
    }

    if (fetchedElements.loading || elementsPUT.loading) {
        return <LoadingSpinner />;
    }

    if (fetchedElements.error) {
        return (
            <div className={classes.errorContainer}>
                <div className={classes.container}>
                    <ErrorIcon className={classes.iconError} />
                    <Typography align="center" variant="h5">
                        {errorText}
                    </Typography>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={getData}
                    >
                        <RefreshIcon className={classes.iconRefreshLarge} />
                    </Button>
                </div>
            </div>
        );
    }

    return (
        <div className={classes.container}>
            <Typography variant="h3">Order Scenario Pages</Typography>
            <Grid container justify="flex-end">
                <Button color="primary" onClick={handleClickOpen}>
                    <HelpIcon />
                </Button>
                <GenericInfoButton
                    description={`Here, you set the order of pages that a student will go through as they complete the simulation. 
                    In the flow diagram click and drag to move around. Double click to zoom in. Simulations start with the introduction. 
                    To connect two pages click the black dot at the bottom of a page and drag your cursor to the top of the page you wish to connect the first page to. 
                    A grey arrow will appear visualizing the connection. Generic pages are red, Reflection pages are purple, and Action pages are green. 
                    Remember that Action pages will require two outgoing arrows for the two possible choices a student might make. 
                    Use the “Reset” button to revert all changes. Click “Save” before leaving the page.`}
                    open={open}
                    setOpen={setOpen}
                />
            </Grid>
            <Button
                variant="contained"
                color="primary"
                onClick={refresh}
                className={classes.margin}
            >
                <RefreshIcon className={classes.iconRefreshSmall} />
            </Button>
            {unsaved ? (
                <Typography variant="h6" align="center" color="error">
                    Unsaved
                </Typography>
            ) : null}
            <SuccessBanner
                successMessage={successBannerMessage}
                fade={successBannerFade}
            />
            <ErrorBanner
                errorMessage={errorBannerMessage}
                fade={errorBannerFade}
            />
            <ConfirmationDialog
                id="confirmRefresh"
                keepMounted
                open={openRefresh}
                onClose={handleCloseRefresh}
                title={'Unsaved Changes'}
                content={
                    'You have unsaved changes. Would you still like to refresh?'
                }
            />
            <ConfirmationDialog
                id="confirmReset"
                keepMounted
                open={openReset}
                onClose={handleCloseReset}
                title={'Reset Flow Diagram'}
                content={'Would you like to reset the flow diagram?'}
            />
            <ReactFlow
                elements={elements}
                style={graphStyles}
                onConnect={onConnect}
                onElementClick={onRemoveEdge}
                onNodeDragStop={onNodeDrag}
                nodeTypes={nodeTypes}
            >
                <div className={classes.buttonContainer}>
                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        onClick={save}
                    >
                        <Typography variant="h6" display="block" noWrap>
                            Save Changes
                        </Typography>
                    </Button>
                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        onClick={handleClickOpenReset}
                    >
                        <Typography variant="h6" display="block" noWrap>
                            Reset
                        </Typography>
                    </Button>
                    <Button
                        className={classes.button}
                        variant="contained"
                        color="primary"
                        disabled={isRemoveButtonDisabled}
                        onClick={deleteEdge}
                    >
                        <Typography variant="h6" display="block" noWrap>
                            Remove Edge
                        </Typography>
                    </Button>
                </div>
                <MiniMap />
                <Controls />
                <Background />
            </ReactFlow>
        </div>
    );
}
