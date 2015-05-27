var React = require('react');

var UserInfoApp = require('./UserApp/UserInfoApp');
var UserAddressApp = require('./UserApp/UserAddressApp');
var UserPassword = require('./UserApp/UserPassword');

var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {Tabs, Tab, Paper} = mui;

var Steps = require('react-steps');

injectTapEventPlugin();
var App = React.createClass({
  childContextTypes: {
      muiTheme: React.PropTypes.object
    },
    getChildContext: function() {
      return {
        muiTheme: ThemeManager.getCurrentTheme()
      };
  },
  listUser:function(){
    $.ajax({
      url      : '/api/v1/u',
      dataType : 'json',
      type     : 'GET',
      success: function(resp) {
        this.setState({
          user:resp.user
        });
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
      }.bind(this)
    });
  },
  listAddress:function(){
    $.ajax({
      url      : '/api/v1/u/address',
      dataType : 'json',
      type     : 'GET',
      success: function(resp) {
        this.setState({
          address:resp.addresses
        });
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
      }.bind(this)
    });
  },
  getInitialState:function(){
    return {
      user: [],
      address:[]
    }
  },
  componentDidMount:function(){
    this.listUser();
    this.listAddress();
    ThemeManager.setPalette({
      accent1Color: Colors.blueGrey50
    });
  },
  onNewAddress:function( newAddress ){

    var newAddress = this.state.address.concat( newAddress );

    this.setState({
      address: newAddress,
    })
  },
  render: function () {

    var step = [
        {
            "text": " 不买吗？",
            "isActive": false,
            "isDone": true
        },
        {
            "text": "一定要选好收货地址哦",
            "isActive": true,
            "isDone": false
        },
        {
            "text": "去付款吧",
            "isActive": false,
            "isDone": false
        },
        {
            "text": "等着凑满人数吧",
            "isActive": false,
            "isDone": false
        },
        {
            "text": "团长在买买买的路上了",
            "isActive": false,
            "isDone": false
        },
        {
            "text": "团长发货了",
            "isActive": false,
            "isDone": false
        },
        {
            "text": "应该收到货了吧,记得确认",
            "isActive": false,
            "isDone": false
        },
        {
            "text": "买买买，不要停",
            "isActive": false,
            "isDone": false
        }
    ];
    var depth = 4
    return (
      <div>
      <Steps items={step}/>
        <Tabs tabItemContainerStyle={{backgroundColor: '#3A3A3A'}} > 
  <Tab  label="个人信息" > 
    <div> 
    <Paper zDepth={depth}>
     <UserInfoApp user={this.state.user} />
     </Paper>
    </div> 
  </Tab> 
  <Tab label="收货地址" > 
    <div> 
      <Paper zDepth={depth}>
      <div>&nbsp;</div>
      <UserAddressApp addresses={this.state.address} listAddress={this.listAddress} onNewAddress={this.onNewAddress} />
      </Paper>
    </div> 
  </Tab> 
   <Tab label="密码修改" > 
    <div> 
     <Paper zDepth={depth}>
      <UserPassword />
      </Paper>
    </div> 
  </Tab> 
 
</Tabs> 
        
      </div>
    );
  }
});




var mainCom = React.render(
  <App />,
  document.getElementById('app')
)

