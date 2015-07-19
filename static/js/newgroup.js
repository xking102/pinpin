var React = require('react');


var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {TextField, Paper, RaisedButton, Snackbar} = mui;
var Dropzone = require('react-dropzone');
var LoadingMask = require("./Components/LoadingMask");
var NewPropery = require("./NewGroup/NewProperty");


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
  _checkField:function(){
    var title = this.refs.title.getValue();
    var desc = this.refs.desc.getValue();
    var errorImages = this.state.errorImages;
    var errorPrice = this.state.errorPrice;
    var errorQty = this.state.errorQty;
    var errorTitle = this.state.errorTitle;
    var errorDesc = this.state.errorDesc;
    if(errorTitle.length>0||errorDesc.length>0||errorImages.length>0||errorPrice.length>0||errorQty.length>0){
      this.setState({
        errorSubmit:'请填写完整'
      });
      return true;
    }else{
      this.setState({
        errorSubmit:''
      });
      return false;
    }
  },
  PostGroup:function(num){
    if(num){
      return '';
    }
    this.setState({
      submitflag:true
    });
    this.refs.loading.show();
    var formData = new FormData();
    for (var i=0;i<this.state.images.length;i++){
      var file = this.state.images[i];
      formData.append('photos',file);
    }
    var color=';';
    var size=';';
    var other=';';
    for (var i=0;i<this.state.color.length;i++){
      color += this.state.color[i].name+';';
    }
    for (var i=0;i<this.state.size.length;i++){
      size += this.state.size[i].name+';';
    }
    for (var i=0;i<this.state.other.length;i++){
      other += this.state.other[i].name+';';
    }
    formData.append('images',this.state.images);
    formData.append('title',this.refs.title.getValue());
    formData.append('desc',this.refs.desc.getValue());
    formData.append('unit_price',this.refs.price.getValue());
    formData.append('list_price',0);
    formData.append('total_qty',this.refs.qty.getValue());
    formData.append('color',color);
    formData.append('size',size);
    formData.append('other',other);
    $.ajax({
      url      : '/api/v1/groups',
      type     : 'POST',
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      data:formData,
      success: function(resp) {
        console.log('succ');
        this._onHandleCancel();
        this.refs.loading.dismiss();
        this.setState({
          submitflag:false
        });
        this.refs.snackbar_succ.show();
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
        this.setState({
          submitflag:false
        });
        this.refs.loading.dismiss();
      }.bind(this)
    });
  },
  getInitialState:function(){
    return {
      images:[],
      color:[],
      size:[],
      other:[],
      flag:true,
      errorTitle:'',
      errorDesc:'',
      errorImages:'别忘了上传图片',
      errorPrice:'',
      errorQty:'',
      errorSubmit:'',
      submitflag:false
    }
  },
  _handleForm:function(e){
    e.preventDefault();
    var num = this._checkField();
    this.PostGroup(num);
  },

  handleAddColor:function( newColor ){
    newColor.key = this.state.color.length + 1;
    if(newColor.key>5){
      this.refs.snackbar.show();
      return '';
    }
    var newColors = this.state.color.concat( newColor );
      this.setState({
        color:newColors
      });
  },
  handleAddSize:function( newSize ){
    newSize.key = this.state.size.length + 1;
    if(newSize.key>5){
      this.refs.snackbar.show();
      return '';
    }
    var newSizes = this.state.size.concat( newSize );
      this.setState({
        size:newSizes
      });
  },
  handleAddOther:function( newOther ){
    newOther.key = this.state.other.length + 1;
    if(newOther.key>5){
      this.refs.snackbar.show();
      return '';
    }
    var newOthers = this.state.other.concat( newOther );
      this.setState({
        other:newOthers
      });
  },

  render: function () {
    var showSubmitError = this.state.errorSubmit.length==0?'':
    <div style={{marginTop:'50px'}} className="alert alert-error">{this.state.errorSubmit}</div>;
    return (
      <div style={{marginLeft:'20%',marginRight:'20%'}}  >
          <Paper zDepth={3}>
          <div style={{marginLeft:'10px',marginRight:'10px',paddingBottom:'20px'}}>



          <form  onSubmit={this._handleForm} ref="addGroupForm" name="addGroup" encType="multipart/form-data" method="POST">
            <TextField
              ref="title"
              style={{width:'100%'}}
              hintText="商品名称"
              type='text'
              multiLine={true}
              onChange={this._handlerTitleChange}
              errorText={this.state.errorTitle}
              floatingLabelText="输入商品名称"
            />

            <br/>

            <TextField
              ref="desc"
              style={{width:'100%'}}
              hintText="商品详情介绍"
              type='text'
              row={3}
              multiLine={true}
              onChange={this._handlerDescChange}
              errorText={this.state.errorDesc}
              floatingLabelText="输入商品详情介绍"
            />

            <br/>

            <TextField
              ref="price"
              hintText="到手单价"
              floatingLabelText="输入到手单价"
              multiLine={true}
              errorText={this.state.errorPrice}
              onChange={this._handleErrorPrice}
            />

            &nbsp;

            <TextField
              ref="qty"
              hintText="团购数量"
              floatingLabelText="输入本次团购数量"
              multiLine={true}
              errorText={this.state.errorQty}
              onChange={this._handleErrorQty}
            />

            <br/>
            <br/>
            <div className="row-fluid">
              <div className='span3'>
                <NewPropery label={'颜色'} list={this.state.color} onAdd={this.handleAddColor}/>
              </div>

              <div className='span3'>
                 <NewPropery label={'尺码'} list={this.state.size} onAdd={this.handleAddSize}/>
              </div>

              <div className='span3'>
                <NewPropery label={'其他'} list={this.state.other} onAdd={this.handleAddOther}/>
              </div>

            </div>

            <br/>
            <br/>

            <Dropzone ref="dropzone" onDrop={this._onDrop} size={150} >
              <div>你可以拖拽多张图片到此处或者双击选择多张图片</div>
            </Dropzone>
            {this.showFiles()}

            <br/>


            <div className="pull-right">
            <a className="btn btn-link" onClick={this._onHandleCancel}>重新填写</a>
            &nbsp;
            <RaisedButton
            label="添加"
            secondary={true}
            disabled={this.state.submitflag}
            />

            <Snackbar
                ref="snackbar"
                message={'至多添加5条属性'}
            />

             <Snackbar
                ref="snackbar_succ"
                message={'发布成功'}
            />
          
            </div>

            {showSubmitError}


          </form>


          </div>
          </Paper>
          <LoadingMask ref="loading"/>
      </div>
    );
  },

  _checkimage:function(img){
    if(img.size>1024*1024&&img.type in ('image/jpeg','image/gif','image/png')){
      return false;
    }{
      return true;
    }
  },

  _onDrop:function(imgs){
    if(imgs.length<6){
      var imgslist=[];
      for (var i=0;i<imgs.length;i++){
        if(this._checkimage(imgs[i])){
          imgslist.push(imgs[i]);
        }
      }
      this.setState({
        images:imgslist,
        errorImages:''
      });
    }else{
      this.setState({
        images:'',
        errorImages:'至多可以上传5张图片'
      });
    }
  },

  showFiles: function () {
    if (this.state.images.length <= 0) {
      return <div style={{marginTop:'10px'}} className="alert alert-error">{this.state.errorImages}</div>;
    }

    var images = this.state.images;

    return (
      <div>
        <h3>预览</h3>
          {[].map.call(images, function (f, i) {
            return <img style={{marginRight:'3px',marginBottom:'3px'}}width={100} height={100} key={i} src={f.preview} />;
          })}
      </div>
    );
  },



  _onHandleCancel:function(){
    this.refs.addGroupForm.getDOMNode().reset();
    this.setState({
      images:[],
      color:[],
      size:[],
      other:[],
      errorImages:'别忘了上传图片',
      errorSubmit:'',
      errorPrice:'',
      errorQty:''
    })
  },

  _handleErrorPrice:function(){
    if(this.refs.price.getValue()>0){
      this.setState({
        errorPrice:''
      });
    }else{
      this.setState({
        errorPrice:'请输入大于0的数字'
      })
    }
  },


  _handleErrorQty:function(){
    var num = this.refs.qty.getValue();
    if(num>0&&num%1==0){
      this.setState({
        errorQty:''
      });
    }else{
      this.setState({
        errorQty:'请输入大于0的整数'
      })
    }
  },

  _handlerTitleChange:function(){
    var title = this.refs.title.getValue();
    if(title.length>0&&title.length<=30){
      this.setState({
        errorTitle:''
      });
    }else{
      this.setState({
        errorTitle:'标题最多30字'
      })
    }
  },

  _handlerDescChange:function(){
    var desc = this.refs.desc.getValue();
    if(desc.length>0&&desc.length<=5000){
      this.setState({
        errorDesc:''
      });
    }else{
      this.setState({
        errorDesc:'标题最多30字'
      })
    }
  },



});




var mainCom = React.render(
  <App />,
  document.getElementById('app')
)
