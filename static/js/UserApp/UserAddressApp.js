var React = require('react');
var mui = require('material-ui');
var {RaisedButton, FlatButton, Dialog} = mui;
var AddressNew = require('./AddressNew');
var AddressItem = require('./AddressItem');

module.exports = React.createClass({

    getInitialState:function(){
        return{
            modal:false
        }
    },
	_handleCustomDialogSubmit:function(){
        this.refs.customDialog.dismiss();
    },
    _handleCustomDialogCancel:function(){
        this.refs.customDialog.dismiss();
    },
    handleCustomDialogTouchTap:function() {
      this.refs.customDialog.show();
    },

	render:function(){
       var addresses = this.props.addresses;
       var addressComps = addresses.map(function(item){
            return <AddressItem key={item.id}
                                address={item}
                                listAddress={this.props.listAddress} />
       }.bind(this));
	   var spantitle_style ={
            margiRight: '10px',
       };
       var tdtitle_style={
            verticalAlign: 'top',
            width: '100px',
       }
		return (
            <div>
            <AddressNew  onNewAddress={this.props.onNewAddress}/>
           
	<div style={{marginTop:'10px',marginLeft:'10px'}}>		
   {addressComps}
   </div>
</div>

		)
	}
})



