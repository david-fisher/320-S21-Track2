import React, { createContext, Component } from 'react';

const ConvLimitContext = createContext();

export class ConvLimitProvider extends Component {

    state = {
        convLimit: 0,
    }

    update = (limit) => {
        this.setState({
            convLimit: limit
        });
    }

    render() {
        return(
            <ConvLimitContext.Provider value={{
                state: this.state,
                update: this.update
            }}>
                {this.props.children}
            </ConvLimitContext.Provider>
        );
    }
}

export const ConvLimitConsumer = ConvLimitContext.Consumer;